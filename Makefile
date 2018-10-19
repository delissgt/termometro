.PHONY: default install developer

default: install

install:
	pipenv install --skip-lock

developer:
	pipenv install --dev --skip-lock
