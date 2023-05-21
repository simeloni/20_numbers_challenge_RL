SRC_DIR = src
CHECK_DIRS = $(SRC_DIR)

.PHONY: check
check: format lint type-check test## Perform all the checks: format

.PHONY: format
format: ## Check the code format with black
		poetry run black $(CHECK_DIRS)
		poetry run black --check $(CHECK_DIRS)
		poetry run isort --check $(CHECK_DIRS)
		poetry run primapy sort-poetry-dependencies --check

.PHONY: reformat
reformat: ## Format repository code
	poetry run black $(CHECK_DIRS)
	poetry run isort $(CHECK_DIRS)

.PHONY: lint
lint: ## Launch the linting tool
	poetry run flake8 $(CHECK_DIRS)

.PHONY: test
test: ## Launch the tests
	echo "Testing tools not yet implemented"

.PHONY: type-check
type-check: ## Launch the type checking tool
	poetry run mypy --install-types --non-interactive --follow-imports silent $(CHECK_DIRS)

.PHONY: help
help: ## Show the available commands
		@echo "Available commands:"
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'