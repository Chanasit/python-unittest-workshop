export OSTYPE = $(shell uname)

install: ## install packages
	pip3 intall -r requirements.txt

test: ## run unittest
	python3 -m unittest services/**.py -v

coverage: ## run unittest coverage
	python3 -m coverage run -m unittest services/** -vvv
	python3 -m coverage report

run: ## run applciation
	python3 -m gunicorn -k uvicorn.workers.UvicornWorker app:app

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
