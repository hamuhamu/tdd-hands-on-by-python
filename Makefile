.PHONY: install test

PYTHON="./bin/python"
PIP="./bin/pip"

install:
	virtualenv .
	${PIP} install -r requirements.txt

test:
	pytest -v test/
