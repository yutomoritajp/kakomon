---
paths: ['backend/**/*']
---

# 開発環境

このバックエンドは**すべてDockerコンテナ上で動作する**。ホストに直接 Python / uv をインストールして動かす運用はしない。

## 技術スタック
- Python 3.13
- FastAPI（`fastapi[standard]`）
- SQLModel（ORM）
- psycopg（PostgreSQL ドライバ、`psycopg[binary]`）
- uv（パッケージ・依存管理）

## コンテナ構成（`backend/Dockerfile`）
- ベースイメージ: `ghcr.io/astral-sh/uv:python3.13-trixie-slim`、`WORKDIR /app`
- `ENV UV_PROJECT_ENVIRONMENT="/usr/local/"` → venv はイメージ内の `/usr/local` 配下（site-packages は `/usr/local/lib/python3.13/site-packages/`）
- ビルド時に `RUN uv sync --frozen` で依存をインストールする
- backend のソースはバインドマウントしている（更新したファイルはホスト側に書き戻る）

## 依存パッケージの追加・更新
backend の依存を変更する際は必ず `backend/README.md` の手順を参照すること。

## マスターデータの採番規約
- `periods.sort_order` は**新しい試験回ほど小さい値**とし、昇順で並べると新しい試験回が先頭に来る。基点は `R7 = 100`。今後追加する試験回（R8 以降）は 99・98… と降順で採番する（負数は避け、0 まで 100 枠を確保）。

