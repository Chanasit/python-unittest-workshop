export OSTYPE = $(shell uname)

install: ## pip install
	pip3 intall -r requirements.txt

test: ## fastapi run
	python3 -m unittest services/**.py -v

coverage:
	python3 -m coverage run -m unittest services/** -vvv
	python3 -m coverage report

run: ## fastapi run
	python3 -m gunicorn -k uvicorn.workers.UvicornWorker app:app

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
