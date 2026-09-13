# Makefile - PDV Automation

.PHONY: help install dev test run clean build

help:
	@echo "================================"
	@echo "  PDV - Makefile Commands"
	@echo "================================"
	@echo ""
	@echo "make install    - Install dependencies"
	@echo "make dev        - Install dev dependencies"
	@echo "make test       - Run tests"
	@echo "make run        - Run the PDV system"
	@echo "make clean      - Clean temporary files"
	@echo "make build      - Build executable"
	@echo "make format     - Format code with Black"
	@echo "make lint       - Check code quality"
	@echo ""

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

dev:
	@echo "📚 Installing dev dependencies..."
	pip install -r requirements.txt
	pip install pytest pytest-cov flake8 black pyinstaller

test:
	@echo "🧪 Running tests..."
	pytest tests/ -v --cov=src

run:
	@echo "🚀 Starting PDV..."
	python src/main.py

clean:
	@echo "🧹 Cleaning temporary files..."
	rm -rf __pycache__ .pytest_cache dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

build:
	@echo "🔨 Building executable..."
	pyinstaller --name=PDV --windowed --onefile src/main.py

format:
	@echo "🎨 Formatting code with Black..."
	black src/ tests/

lint:
	@echo "🔍 Checking code quality..."
	flake8 src/ --max-line-length=127
	black --check src/ tests/

venv:
	@echo "⚙️  Creating virtual environment..."
	python -m venv venv
	@echo "✅ Virtual environment created!"
	@echo "Activate with: source venv/bin/activate (Linux/Mac)"
	@echo "             or: venv\Scripts\activate (Windows)"
