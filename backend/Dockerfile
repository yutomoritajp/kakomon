FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
ENV UV_SYSTEM_PYTHON=1
ENV UV_LINK_MODE=copy
ENV UV_CACHE_DIR=/root/.cache/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY . .

CMD ["uv", "run", "--no-sync", "fastapi", "dev", "main.py", "--host", "0.0.0.0"]