#!/bin/bash

echo "🚀 Setting up Claude Bedrock API Test Project"
echo "=============================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

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

# Make scripts executable
chmod +x test_claude_converse.py
chmod +x simple_example.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your AWS credentials"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Run the simple example: python simple_example.py"
echo "4. Run the full test suite: python test_claude_converse.py"
echo ""
echo "Make sure you have access to Claude 3.5 Sonnet in your AWS region!"
