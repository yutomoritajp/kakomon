---
paths: ['backend/**/*']
---

# 開発環境

このバックエンドは**すべてDockerコンテナ上で動作する**。ホストに直接 Python / uv をインストールして動かす運用はしない。

## 技術スタック
パッケージの正は `backend/pyproject.toml`。ここには各パッケージの役割を記す。

### 実行時依存（`[project]` の `dependencies`）
- Python 3.13
- FastAPI（`fastapi[standard]`）… Web API
- SQLModel（ORM）
- psycopg（PostgreSQL ドライバ、`psycopg[binary]`）
- Alembic（`alembic`）… DB マイグレーション。定義は `backend/data/migrations/` 配下
- Anthropic SDK（`anthropic`）… Claude API クライアント。`backend/services/claude_api_service.py` で使用
- PyMuPDF（`pymupdf`）… 過去問 PDF の解析。`backend/services/pdf_service.py` で使用
- python-dotenv（`python-dotenv`）… `.env` の読み込み。import 名は `dotenv`

### 開発用依存（`[dependency-groups]` の `dev`）
- pytest（`pytest`）… テスト

### ツール
- uv（パッケージ・依存管理）

## コンテナ構成（`backend/Dockerfile`）
- ベースイメージ: `ghcr.io/astral-sh/uv:python3.13-trixie-slim`、`WORKDIR /app`
- `ENV UV_PROJECT_ENVIRONMENT="/usr/local/"` → venv はイメージ内の `/usr/local` 配下（site-packages は `/usr/local/lib/python3.13/site-packages/`）
- ビルド時に `RUN uv sync --frozen` で依存をインストールする
- backend のソースはバインドマウントしている（更新したファイルはホスト側に書き戻る）

## 依存パッケージの追加・更新・削除
backend の依存を変更する際は必ず `backend/README.md` の手順を参照すること。

## マスターデータの採番規約
- `periods.sort_order` は**新しい試験回ほど小さい値**とし、昇順で並べると新しい試験回が先頭に来る。基点は `r7 = 100`。今後追加する試験回（r8 以降）は 99・98… と降順で採番する（負数は避け、0 まで 100 枠を確保）。

## 識別子の命名規約
- `periods.code` / `sections.code` などの識別子は**小文字**で統一する（例：`r7`、`am1`）。ストレージのディレクトリ名にもそのまま利用するため、DB値・ディレクトリ名・コード内文字列で大文字小文字を揃える。

## データ配置規約
- **入力データと本番生成物をディレクトリで分ける**。
  - `backend/past_exams/` … 過去問PDFのシード元データ。シード後は運用で参照しない、デプロイ対象に含めない前提の入力データ。
  - `backend/storage/` … アプリが本番運用でも参照する生成物（問題・解説の画像 等）。開発ローカルでの置き場であり、本番実運用ではオブジェクトストレージ（S3 等）への配置を想定する。

