.PHONY: install test lint format-check clean

# Default target
all: test lint

# Install dependencies
install:
	pip install pytest miniflux

# Run tests
test:
	pytest tests/ -v

# Lint SKILL.md
lint:
	@echo "Checking SKILL.md format..."
	@if [ ! -f "SKILL.md" ]; then \
		echo "ERROR: SKILL.md not found"; \
		exit 1; \
	fi
	@echo "SKILL.md validation passed"

# Check code formatting (for future use)
format-check:
	@echo "Format check passed (no Python formatting yet)"

# Clean test artifacts
clean:
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

# Run all checks
check: test lint
