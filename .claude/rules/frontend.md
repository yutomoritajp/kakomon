---
paths: ['frontend/**/*']
---

# 開発環境

このフロントエンドは**すべてDockerコンテナ上で動作する**。ホストに直接 Node をインストールして動かす運用はしない。

## 技術スタック
- React 19 / JavaScript（JSX、TypeScriptではない）
- Vite 8（dev server / ビルド）
- ESLint（flat config: `eslint.config.js`）
- Tailwind CSS（v4）

## コンテナ構成（`compose.yaml` / `frontend/Dockerfile`）
- ベースイメージ: `node:20-slim`、`WORKDIR /app`、実行ユーザー `node`
- サービス名: `frontend`、ポート `5173:5173`
- dev server は `vite.config.js` で `server.host: true`（コンテナ外からアクセスするため）

## ボリューム構成（重要）
```yaml
volumes:
  - ./frontend:/app                       # ソースはホストとバインドマウント（双方向同期）
  - react_node_modules:/app/node_modules  # node_modulesは名前付きボリュームで隔離
```
- `package.json` / `package-lock.json` / ソースコードは**ホスト側と同期**する → 編集・gitコミットはホスト側で見える。
- **`node_modules` だけはコンテナ内の名前付きボリューム**にあり、ホストの `frontend/node_modules` とは別物。**ホスト側で `npm install` してもコンテナには反映されない。**

## パッケージの追加・削除
必ずコンテナ側で実行する：
```bash
docker compose run --rm frontend npm install <package>
```
- `package.json` / `package-lock.json` はバインドマウント経由でホストに書き戻されるのでコミット可能。
- `vite.config.js` 等の設定を変えた場合は dev server（コンテナ）を再起動して反映する。
