.PHONY: all push test build

all:

push:
	act $@

.venv:
	pipenv install --dev

test: .venv
	pipenv run pytest

build: .venv
	pipenv run python -m build
