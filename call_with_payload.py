#!/usr/bin/env python3
"""
Call Claude 3.7 Converse API using data from a specified payload JSON file
Usage: python call_with_payload.py [payload_file]
"""

import boto3
import json
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def call_converse_with_payload(payload_file="payload.json"):
    """Call Converse API using specified payload file"""
    
    # Initialize Bedrock client
    bedrock = boto3.client(
        'bedrock-runtime',
        region_name=os.getenv('AWS_REGION', 'us-east-1')
    )
    
    # Model ID for Claude 3.7 Sonnet
    model_id = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
    
    # Check if payload file exists
    if not os.path.exists(payload_file):
        print(f"❌ Error: Payload file '{payload_file}' not found")
        print(f"📁 Current directory: {os.getcwd()}")
        print(f"📋 Available JSON files:")
        json_files = [f for f in os.listdir('.') if f.endswith('.json')]
        if json_files:
            for f in json_files:
                print(f"   - {f}")
        else:
            print("   - No JSON files found in current directory")
        return False
    
    # Load payload from JSON file
    try:
        with open(payload_file, 'r', encoding='utf-8') as f:
            payload = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in '{payload_file}' - {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading '{payload_file}': {e}")
        return False
    
    print(f"📋 Loaded payload from: {payload_file}")
    print(f"🤖 Using Claude 3.7 model: {model_id}")
    print("=" * 60)
    
    # Extract components from payload
    system = payload.get('system', [])
    messages = payload.get('messages', [])
    tool_config = payload.get('toolConfig', {})
    inference_config = payload.get('inferenceConfig', {})
    
    # Use default inference config if not provided in payload
    if not inference_config:
        inference_config = {
            "maxTokens": 4096,
            "temperature": 0.7
        }
    
    print(f"📊 Payload Summary:")
    print(f"   - System prompts: {len(system)}")
    print(f"   - Messages: {len(messages)}")
    print(f"   - Tools available: {len(tool_config.get('tools', []))}")
    print(f"   - Max tokens: {inference_config.get('maxTokens', 'default')}")
    print(f"   - Temperature: {inference_config.get('temperature', 'default')}")
    
    # Show the conversation history
    if messages:
        print(f"\n💬 Conversation History:")
        for i, msg in enumerate(messages, 1):
            role = msg.get('role', 'unknown')
            content = msg.get('content', [])
            if content and isinstance(content, list) and len(content) > 0:
                text = content[0].get('text', '')
                # Truncate long messages for display
                display_text = text[:100] + ('...' if len(text) > 100 else '')
                print(f"   {i}. {role.upper()}: {display_text}")
    
    # Show system prompt if present
    if system:
        print(f"\n🎯 System Prompt Preview:")
        system_text = system[0].get('text', '') if system else ''
        display_system = system_text[:150] + ('...' if len(system_text) > 150 else '')
        print(f"   {display_system}")
    
    # Show available tools if present
    if tool_config.get('tools'):
        print(f"\n🔧 Available Tools:")
        for tool in tool_config['tools']:
            tool_name = tool.get('toolSpec', {}).get('name', 'Unknown')
            tool_desc = tool.get('toolSpec', {}).get('description', 'No description')
            print(f"   - {tool_name}: {tool_desc[:80]}{'...' if len(tool_desc) > 80 else ''}")
    
    print("\n" + "=" * 60)
    print("🚀 Calling Claude 3.7 Converse API...")
    print("=" * 60)
    
    # Prepare the API call parameters
    api_params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": inference_config
    }
    
    # Add optional parameters if they exist
    if system:
        api_params["system"] = system
    if tool_config:
        api_params["toolConfig"] = tool_config
    
    # Call the Converse API
    try:
        response = bedrock.converse(**api_params)
        
        # Extract and print the response
        if "output" in response and "message" in response["output"]:
            message = response["output"]["message"]
            
            print("🤖 Claude 3.7 Response:")
            print("-" * 40)
            
            if "content" in message:
                for content_block in message["content"]:
                    if "text" in content_block:
                        print(content_block["text"])
                    elif "toolUse" in content_block:
                        tool_use = content_block["toolUse"]
                        print(f"\n🔧 Tool Call: {tool_use.get('name', 'Unknown')}")
                        print(f"   Tool ID: {tool_use.get('toolUseId', 'N/A')}")
                        print(f"   Input: {json.dumps(tool_use.get('input', {}), indent=2)}")
        
        # Print usage statistics
        usage = response.get('usage', {})
        print(f"\n📊 Token Usage:")
        print(f"   - Input tokens: {usage.get('inputTokens', 0):,}")
        print(f"   - Output tokens: {usage.get('outputTokens', 0):,}")
        print(f"   - Total tokens: {usage.get('totalTokens', 0):,}")
        
        # Additional usage details if available
        if usage.get('cacheReadInputTokens', 0) > 0:
            print(f"   - Cache read tokens: {usage.get('cacheReadInputTokens', 0):,}")
        if usage.get('cacheWriteInputTokens', 0) > 0:
            print(f"   - Cache write tokens: {usage.get('cacheWriteInputTokens', 0):,}")
        
        # Check if there are tool calls that need responses
        if "output" in response and "message" in response["output"]:
            message = response["output"]["message"]
            if "content" in message:
                tool_calls = [block for block in message["content"] if "toolUse" in block]
                if tool_calls:
                    print(f"\n⚠️  Note: Claude made {len(tool_calls)} tool call(s).")
                    print(f"   In a real implementation, you would need to:")
                    print(f"   1. Execute each tool with the provided input")
                    print(f"   2. Add tool results to the conversation")
                    print(f"   3. Continue the conversation with Claude")
        
        # Check stop reason
        stop_reason = response.get('stopReason', 'unknown')
        print(f"\n🛑 Stop Reason: {stop_reason}")
        
    except Exception as e:
        print(f"❌ Error calling Converse API: {str(e)}")
        return False
    
    print("\n" + "=" * 60)
    print("✅ Converse API call completed successfully!")
    return True

def print_usage():
    """Print usage instructions"""
    print("Usage: python call_with_payload.py [payload_file]")
    print("")
    print("Arguments:")
    print("  payload_file    Path to JSON payload file (default: payload.json)")
    print("")
    print("Examples:")
    print("  python call_with_payload.py                    # Uses payload.json")
    print("  python call_with_payload.py my_payload.json    # Uses my_payload.json")
    print("  python call_with_payload.py data/test.json     # Uses data/test.json")

if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) > 2:
        print("❌ Error: Too many arguments")
        print_usage()
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] in ['-h', '--help', 'help']:
            print_usage()
            sys.exit(0)
        payload_file = sys.argv[1]
    else:
        payload_file = "payload.json"
    
    print(f"🚀 Claude 3.7 Converse API Caller")
    print(f"📁 Payload file: {payload_file}")
    print("=" * 60)
    
    # Call the function
    success = call_converse_with_payload(payload_file)
    
    if not success:
        sys.exit(1)
