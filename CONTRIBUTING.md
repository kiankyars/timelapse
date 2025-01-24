# Contributing to Timelapse Creator

## Getting Started

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/kiankyars/timelapse.git

# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

## Contribution Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions
- Maintain modular design

### Testing
- Add unit tests for new features
- Ensure 100% test coverage for modified code
- Run tests before submitting PRs

### Commit Messages
- Use clear, descriptive commits
- Follow conventional commit format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation updates
  - `refactor:` for code restructuring

### Pull Request Process
1. Describe changes in PR description
2. Link related issues
3. Ensure CI/CD checks pass
4. Request review from maintainers

## Reporting Issues
- Use GitHub Issues
- Include reproducible steps
- Provide environment details
- Attach logs or screenshots if applicable

## Code of Conduct
- Be respectful
- Collaborate constructively
- Welcome diverse perspectives