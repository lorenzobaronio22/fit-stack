# Backend

FastAPI REST API built with Python.

## Development

### Installation

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

### Commands

#### Development

Start the development server with hot reload:

```bash
uv run fastapi dev
```

#### Testing

Run the test suite:

```bash
uv run pytest
```

#### Lint & Format

Check code for linting issues:

```bash
uv run ruff check
```

Automatically fix lint issues:

```bash
uv run ruff check --fix
```

Format code according to the style guide:

```bash
uv run ruff format
```

#### Docker

Build the Docker image (uses `backend/Dockerfile`):

```bash
docker build -t fitstack-backend .
```

Run the container and map port `8000` on the host to port `80` in the container:

```bash
docker run -p 8000:80 fitstack-backend
```
