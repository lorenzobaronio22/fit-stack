# Backend

FastAPI REST API built with Python.

## Development

### Installation

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

### Commands

- `uv run fastapi dev` - Start the development server with hot reload
- `uv run pytest` - Run the test suite
- `uv run ruff check` - Check code for linting issues
- `uv run ruff check --fix` - Automatically fix linting issues
- `uv run ruff format` - Format code according to style guide
- `docker build -t fitstack-backend .` - Build docker container
- `docker run -p 8000:80 fitstack-backend` - Run docker container
