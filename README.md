# Claude 3.7 Bedrock Converse API Testing Tool

A streamlined Python tool for testing and interacting with Claude 3.7 via AWS Bedrock's Converse API. This project provides a flexible payload-based approach for system prompts, multi-turn conversations, and tool/function calling.

## 🚀 Features

- ✅ **Claude 3.7 Support** - Latest Claude model with enhanced capabilities
- ✅ **Flexible Payload System** - JSON-based conversation loading with command-line arguments
- ✅ **System Prompts** - Custom system instructions support
- ✅ **Multi-turn Conversations** - Maintain conversation context
- ✅ **Tool/Function Calling** - Execute tools and functions
- ✅ **Comprehensive Error Handling** - Robust error management
- ✅ **Token Usage Tracking** - Monitor API usage and costs
- ✅ **Multiple Payload Support** - Easy switching between different test scenarios

## 📋 Prerequisites

- Python 3.7+
- AWS account with Bedrock access
- Claude 3.7 model access in your AWS region
- AWS credentials configured

## 🛠️ Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd call-bedrock-api
chmod +x setup.sh
./setup.sh
```

### 2. Configure AWS Credentials

Edit the `.env` file with your AWS credentials:
```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_SESSION_TOKEN=your_session_token_here  # If using temporary credentials
```

### 3. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 4. Run Examples

```bash
# Use default payload.json
python call_with_payload.py

# Use specific payload file
python call_with_payload.py payload-no-hallucination.json

# Create and use your own payload
python call_with_payload.py my_custom_payload.json

# Show help
python call_with_payload.py --help
```

## 📁 Project Structure

```
call-bedrock-api/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── setup.sh                   # Setup script
├── CONTRIBUTING.md             # Contribution guidelines
│
├── call_with_payload.py        # Main Claude 3.7 API caller
│
├── payload.json                # Example conversation payload with tools
├── payload-no-hallucination.json # Alternative payload example
│
├── .github/
│   └── workflows/
│       └── test.yml            # GitHub Actions CI/CD
│
└── venv/                       # Virtual environment (created by setup)
```

## 🔧 Usage Examples

### Basic Usage

The main script `call_with_payload.py` accepts a payload filename as an argument:

```bash
# Use default payload
python call_with_payload.py

# Use specific payload file
python call_with_payload.py my_payload.json

# Show usage help
python call_with_payload.py --help
```

### Creating Custom Payloads

Create a JSON payload file with your conversation:

```json
{
  "system": [
    {"text": "You are a helpful coding assistant."}
  ],
  "messages": [
    {
      "role": "user",
      "content": [{"text": "Write a Python function to sort a list."}]
    }
  ],
  "inferenceConfig": {
    "maxTokens": 1000,
    "temperature": 0.3
  }
}
```

### Advanced Payload with Tools

```json
{
  "system": [
    {"text": "You are a helpful assistant with access to tools."}
  ],
  "messages": [
    {
      "role": "user",
      "content": [{"text": "What's the weather like in Seattle?"}]
    }
  ],
  "toolConfig": {
    "tools": [
      {
        "toolSpec": {
          "name": "get_weather",
          "description": "Get weather information for a location",
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "location": {"type": "string"}
              },
              "required": ["location"]
            }
          }
        }
      }
    ]
  },
  "inferenceConfig": {
    "maxTokens": 2000,
    "temperature": 0.7
  }
}
```

## 📊 Payload File Format

Payload files support the following structure:

```json
{
  "system": [
    {"text": "System prompt here"}
  ],
  "messages": [
    {
      "role": "user|assistant",
      "content": [{"text": "Message content"}]
    }
  ],
  "toolConfig": {
    "tools": [
      {
        "toolSpec": {
          "name": "tool_name",
          "description": "Tool description",
          "inputSchema": { /* JSON schema */ }
        }
      }
    ]
  },
  "inferenceConfig": {
    "maxTokens": 4096,
    "temperature": 0.7,
    "topP": 0.9,
    "stopSequences": ["STOP"]
  }
}
```

### Payload Components

- **`system`** (optional): Array of system prompts to guide Claude's behavior
- **`messages`** (required): Conversation history with user and assistant messages
- **`toolConfig`** (optional): Tool definitions for function calling
- **`inferenceConfig`** (optional): Model parameters like temperature and max tokens

## 🎯 Script Features

The `call_with_payload.py` script provides:

| Feature | Description |
|---------|-------------|
| **Flexible Input** | Accepts any JSON payload file as argument |
| **Error Handling** | Comprehensive error checking and user-friendly messages |
| **File Validation** | Checks file existence and JSON validity |
| **Usage Help** | Built-in help with `--help` flag |
| **Token Tracking** | Detailed token usage statistics |
| **Tool Support** | Handles tool calls and displays results |
| **Rich Output** | Formatted display of conversation and metadata |

## 🌍 AWS Configuration

### Option 1: Environment Variables
```bash
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

### Option 2: AWS CLI Profile
```bash
aws configure --profile bedrock
export AWS_PROFILE=bedrock
```

### Option 3: IAM Role (EC2/Lambda)
No additional configuration needed if running on AWS with proper IAM role.

## 🔐 Required IAM Permissions

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-7-sonnet-20250219-v1:0"
            ]
        }
    ]
}
```

## 🌐 Model Availability

Claude 3.7 Sonnet is available in these regions:
- us-east-1 (N. Virginia)
- us-west-2 (Oregon)
- eu-west-1 (Ireland)
- ap-southeast-1 (Singapore)
- ap-northeast-1 (Tokyo)

Check the [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html) for the latest availability.

## 🐛 Troubleshooting

### Common Issues

1. **Model not found**: Ensure Claude 3.7 is available in your region
2. **Access denied**: Check IAM permissions and model access in Bedrock console
3. **Invalid model ID**: The script uses `us.anthropic.claude-3-7-sonnet-20250219-v1:0`
4. **File not found**: Check that your payload file exists and path is correct
5. **Invalid JSON**: Validate your payload file JSON syntax
6. **Rate limits**: Implement exponential backoff for production use
7. **Token limits**: Monitor usage and adjust maxTokens parameter

### Error Handling

The tool includes comprehensive error handling for:
- File not found errors
- JSON parsing errors
- API call failures
- Tool execution errors
- Invalid responses
- Network issues

### Debug Tips

```bash
# Check if file exists
ls -la your_payload.json

# Validate JSON syntax
python -c "import json; print(json.load(open('your_payload.json')))"

# Test with simple payload
echo '{"messages":[{"role":"user","content":[{"text":"Hello"}]}]}' > test.json
python call_with_payload.py test.json
```

## 🚀 Production Considerations

- Implement proper logging
- Add retry logic with exponential backoff
- Use secure credential management (AWS Secrets Manager)
- Monitor costs and usage
- Implement rate limiting
- Add input validation and sanitization
- Use proper tool execution sandboxing
- Set up monitoring and alerting

## 📈 Token Usage Monitoring

The script provides detailed token usage information:
- Input tokens (with comma formatting)
- Output tokens (with comma formatting)
- Total tokens (with comma formatting)
- Cache read/write tokens (when applicable)
- Stop reason information

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is for educational and testing purposes. Please follow AWS and Anthropic's terms of service when using their APIs.

## 🔗 Useful Links

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Claude API Documentation](https://docs.anthropic.com/)
- [AWS Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
- [Anthropic Claude Models](https://www.anthropic.com/claude)

---

**Note**: This tool is designed for testing and development. For production use, implement additional security measures, error handling, and monitoring.
