export OSTYPE = $(shell uname)

install: ## install packages
	pip3 intall -r requirements.txt

test: ## run unittest
	python3 -m unittest app/services/test_**.py -v

coverage: ## run unittest coverage
	python3 -m coverage run -m unittest app/services/test_**.py -v
	python3 -m coverage report

run: ## run applciation
	python3 -m gunicorn -k uvicorn.workers.UvicornWorker app.main:app --workers 1 --bind localhost:8080

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
