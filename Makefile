help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean-pyc     to remove .pyc files"

clean-pyc:
	find . -name "*.pyc" -exec rm {} +

