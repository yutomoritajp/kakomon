# kakomon

IPA「データベーススペシャリスト試験」の過去問演習用Webアプリケーション。
開発者本人の個人学習を目的とし、既存の「データベーススペシャリスト過去問道場」より学習しやすいことを目指す。差別化機能として、問題や解説についてAIに質問できる機能を実装予定。

本プロジェクトはClaude Code（AIエージェント）との共同開発を前提とし、開発者主導で設計・実装を行い、AIエージェントがレビュー等の補佐をする。

## 技術スタック

- フロントエンド: React 19 (JavaScript) / Vite / Tailwind CSS
- API: Python / FastAPI（未実装）
- DB: PostgreSQL（未実装）
- 実行環境: Docker

## 開発状況

v0（最低限動作するアプリケーション）を開発中。現時点ではフロントエンドのみ実装している。
バージョンごとの要件・スコープは `docs/` 配下を参照。

## 起動方法

フロントエンドはすべてDockerコンテナ上で動作する（ホストにNodeをインストールしない）。

```bash
docker compose up
```

起動後、 http://localhost:5173 でアクセスできる。

パッケージの追加は必ずコンテナ側で実行する：

```bash
docker compose run --rm frontend npm install <package>
```

## プロジェクト構成

```
.
├── compose.yaml      ← Docker Compose定義
├── docs/             ← 要件定義書・基本設計書（バージョンごとにフォルダを分ける）
├── backend/          ← バックエンド（Python）
├── frontend/         ← フロントエンド（React）
└── .claude/          ← AIエージェント向けの指示・規約
```

## Todoリスト

- TypeScriptへの移行(移行したら`./frontend/jsconfig.json`の設定を変更する。)
- 問題数上限10問の制約事項を、該当スコープの基本設計書に反映する