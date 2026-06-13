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

## AIエージェントの振る舞いについて（重要）

開発者からの質問・レビュー依頼に対してAIエージェントは、エラーの原因や修正背景の本質を説明すること。
開発者が求めているのは「なぜそのエラーが発生しているか」「なぜその修正をすべきか」の理解であり、修正済みコードの提示ではない。
そのため、AIエージェントはコードを修正せず、「修正しますか？」といった提案も行わないこと。
回答の末尾に「次のステップ」「どう進めますか？」といった促しの言葉を加えないこと。聞かれたことに対してのみ回答する。
ただし、開発者から明示的に修正方法や次のアクションを求めた場合はこの限りではない。
