# Contributing to Claude 3.7 Bedrock Testing Tool

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the Claude 3.7 Bedrock Converse API Testing Tool.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- AWS account with Bedrock access
- Git
- Basic understanding of AWS Bedrock and Claude API

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/call-bedrock-api.git
   cd call-bedrock-api
   ```

2. **Set up development environment**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   source venv/bin/activate
   ```

3. **Install development dependencies**
   ```bash
   pip install pytest pytest-cov flake8 black isort
   ```

4. **Configure AWS credentials**
   ```bash
   cp .env.example .env
   # Edit .env with your AWS credentials
   ```

## 🛠️ Development Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Code Formatting

We use `black` for code formatting and `isort` for import sorting:

```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8 .
```

### Testing

- Test your changes thoroughly
- Add tests for new functionality
- Ensure existing tests pass
- Test with different payload files

```bash
# Run syntax validation
python -m py_compile *.py

# Test JSON validation
python -c "import json; json.load(open('payload.json'))"

# Test help functionality
python call_with_payload.py --help
```

## 📝 Contribution Types

### Bug Reports

When reporting bugs, please include:

- **Description**: Clear description of the issue
- **Steps to reproduce**: Detailed steps to reproduce the bug
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**: Python version, OS, AWS region
- **Error messages**: Full error messages and stack traces
- **Payload file**: Sample payload file that causes the issue (remove sensitive data)

### Feature Requests

When requesting features, please include:

- **Use case**: Why this feature would be useful
- **Description**: Detailed description of the proposed feature
- **Examples**: Code examples or mockups if applicable
- **Alternatives**: Alternative solutions you've considered

### Code Contributions

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the coding guidelines
   - Add appropriate tests
   - Update documentation if needed

3. **Test your changes**
   ```bash
   # Validate syntax
   python -m py_compile *.py
   
   # Test functionality
   python simple_example.py
   python call_with_payload.py test_payload.json
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

5. **Push and create pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Message Guidelines

Use conventional commit format:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add support for Claude 3.8 model
fix: handle empty payload files gracefully
docs: update README with new examples
```

## 🔍 Pull Request Process

1. **Ensure your PR**:
   - Has a clear title and description
   - References any related issues
   - Includes tests for new functionality
   - Updates documentation if needed
   - Passes all existing tests

2. **PR Description should include**:
   - What changes were made
   - Why the changes were necessary
   - How to test the changes
   - Any breaking changes

3. **Review Process**:
   - Maintainers will review your PR
   - Address any feedback or requested changes
   - Once approved, your PR will be merged

## 📚 Documentation

### Code Documentation

- Add docstrings to all functions and classes
- Use clear, descriptive comments
- Update README.md for new features
- Include usage examples

### Example Documentation Format

```python
def call_converse_with_payload(payload_file="payload.json"):
    """
    Call Converse API using specified payload file.
    
    Args:
        payload_file (str): Path to JSON payload file. Defaults to "payload.json".
        
    Returns:
        bool: True if successful, False otherwise.
        
    Raises:
        FileNotFoundError: If payload file doesn't exist.
        json.JSONDecodeError: If payload file contains invalid JSON.
        
    Example:
        >>> success = call_converse_with_payload("my_test.json")
        >>> if success:
        ...     print("API call successful")
    """
```

## 🚨 Security Guidelines

- **Never commit AWS credentials** to the repository
- **Remove sensitive data** from payload examples
- **Use environment variables** for configuration
- **Validate input data** to prevent injection attacks
- **Follow AWS security best practices**

## 🐛 Debugging

### Common Issues

1. **AWS Credentials**: Ensure credentials are properly configured
2. **Model Access**: Verify Claude 3.7 access in your AWS region
3. **JSON Format**: Validate payload JSON structure
4. **Python Environment**: Use the virtual environment

### Debug Mode

Add debug logging to your contributions:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug information here")
```

## 📋 Checklist for Contributors

Before submitting a PR, ensure:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages follow convention
- [ ] No sensitive data in commits
- [ ] Feature works with different payload types
- [ ] Error handling is implemented
- [ ] Code is well-commented

## 🤝 Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Follow the code of conduct
- Ask questions if you're unsure

## 📞 Getting Help

- **Issues**: Create a GitHub issue for bugs or questions
- **Discussions**: Use GitHub Discussions for general questions
- **Documentation**: Check the README and code comments

## 🎯 Areas for Contribution

We welcome contributions in these areas:

- **New Claude models**: Support for newer Claude versions
- **Additional tools**: More example tools and integrations
- **Error handling**: Better error messages and recovery
- **Documentation**: Improved examples and tutorials
- **Testing**: More comprehensive test coverage
- **Performance**: Optimization and efficiency improvements
- **Security**: Enhanced security features

Thank you for contributing to make this tool better for everyone! 🚀
