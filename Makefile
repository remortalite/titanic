test:
	@ uv run pytest .

check:
	@ uv run ruff check

format:
	@ uv run ruff check --fix

run:
	@ uv run python main.py

precommit: format test

.PHONY: test check format run
