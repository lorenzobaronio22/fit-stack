# Backend

FastAPI REST API built with Python.

## Development

### Installation

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

### Commands

- Development
	- `uv run fastapi dev` — Start the development server with hot reload

- Testing
	- `uv run pytest` — Run the test suite

- Lint & Format
	- `uv run ruff check` — Check code for linting issues
	- `uv run ruff check --fix` — Automatically fix linting issues
	- `uv run ruff format` — Format code according to style guide

- Docker
	- Build: `docker build -t fitstack-backend .` — Build Docker container (uses `backend/Dockerfile`)
	- Run: `docker run -p 8000:80 fitstack-backend` — Run Docker container; maps port `8000` → container port `80`
