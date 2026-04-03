install:
	uv sync
brain-games:
	uv run VD-games
build:
	rm -rf dist
	uv build
package-install:
	uv tool install dist/*whl
	uv tool install --force dist/sneja-0.1.0-py3-none-any.whl
lint:
	uv run ruff check VD_games
