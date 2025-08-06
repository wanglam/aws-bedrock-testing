#!/bin/bash

echo "🚀 Setting up Claude 3.7 Bedrock API Testing Tool"
echo "=================================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Copy environment template if .env doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "📝 Please edit .env file with your AWS credentials"
else
    echo "✅ .env file already exists"
fi

# Make main script executable
chmod +x call_with_payload.py

# Validate payload files
echo "🔍 Validating payload files..."
if python3 -c "import json; json.load(open('payload.json'))" 2>/dev/null; then
    echo "✅ payload.json is valid"
else
    echo "❌ payload.json has invalid JSON syntax"
fi

if python3 -c "import json; json.load(open('payload-no-hallucination.json'))" 2>/dev/null; then
    echo "✅ payload-no-hallucination.json is valid"
else
    echo "❌ payload-no-hallucination.json has invalid JSON syntax"
fi

# Test the main script help functionality
echo "🧪 Testing script functionality..."
if python3 call_with_payload.py --help > /dev/null 2>&1; then
    echo "✅ call_with_payload.py help works correctly"
else
    echo "❌ call_with_payload.py help failed"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your AWS credentials:"
echo "   - AWS_REGION (e.g., us-east-1)"
echo "   - AWS_ACCESS_KEY_ID"
echo "   - AWS_SECRET_ACCESS_KEY"
echo "   - AWS_SESSION_TOKEN (if using temporary credentials)"
echo ""
echo "2. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "3. Run examples:"
echo "   python call_with_payload.py                    # Use default payload.json"
echo "   python call_with_payload.py payload-no-hallucination.json  # Use alternative payload"
echo "   python call_with_payload.py --help             # Show help"
echo ""
echo "📚 Available payload files:"
echo "   - payload.json                    # Example with tools and conversation history"
echo "   - payload-no-hallucination.json  # Alternative payload example"
echo ""
echo "🔧 Make sure you have access to Claude 3.7 in your AWS region!"
echo "   Model ID: us.anthropic.claude-3-7-sonnet-20250219-v1:0"
