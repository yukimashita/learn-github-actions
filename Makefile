.PHONY: all push pytest

all:

push:
	act $@

pytest:
	pipenv run pytest
