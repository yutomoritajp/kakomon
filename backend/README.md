# 依存パッケージの追加・更新・削除手順

ビルド時の `uv sync --frozen` は **`uv.lock` のみを正としてインストールし、`pyproject.toml` は参照しない**。そのため `pyproject.toml` を編集しただけでは反映されず、`uv.lock` の更新が必須となる。

## 手順
1. 依存を追加・変更する（`uv add <pkg>` または `pyproject.toml` を編集）。テストツールのようにアプリの実行に不要なものは `uv add --dev <pkg>` で開発用依存にする（後述の「具体例」を参照）。
2. ロックを更新する。ホストに uv が無いため**コンテナ内で実行する**：
   ```bash
   docker compose exec backend uv lock
   ```
   backend はバインドマウントしているため、更新された `uv.lock` はホスト側に書き戻る。
3. `uv.lock`（と `pyproject.toml`）をコミットする。
4. **イメージを再ビルドする**。再ビルドで `uv sync --frozen` が新しいロックを読み、誰の環境でも依存が定着する。

## 注意
- `uv lock` は**ロックを更新するだけでパッケージは入らない**。
- コンテナ内で `uv sync` すれば即時にインストールされるが、実体は `/usr/local`（イメージ層）にあるため**コンテナ再作成で揮発する**。恒久反映は再ビルドで行う。
- 依存追加時に `uv.lock` の更新を忘れると、再ビルドしても反映されない。`uv add` を使えば pyproject 追記とロック更新が同時に行われるので、こちらが安全。
- `git pull` した差分に `uv.lock` の変更が含まれていた場合は、`docker compose up -d --build backend` で再ビルドする。ソースはバインドマウントしているため、依存の変更が無ければ再ビルドは不要。

## 削除の手順
1. コンテナを起動する。
   ```bash
   docker compose up -d backend
   ```
2. 依存を削除する。`pyproject.toml` からの削除・`uv.lock` の更新・環境からのアンインストールが**まとめて行われる**。
   ```bash
   docker compose exec backend uv remove <pkg>
   ```
   開発用依存（`[dependency-groups]` の `dev`）から消す場合は `--dev` を付ける。
   ```bash
   docker compose exec backend uv remove --dev <pkg>
   ```
3. **イメージを再ビルドする**。追加時と同様、再ビルドしないと削除がイメージに定着しない。
   ```bash
   docker compose up -d --build backend
   ```
4. 削除されたことを確認する。
   ```bash
   docker compose exec backend uv tree
   ```
5. `pyproject.toml` と `uv.lock` をコミットする。

### 削除時の注意
- `uv remove` が消すのは**このプロジェクトの依存宣言**であり、パッケージそのものの抹消ではない。他のパッケージが依存しているものは、推移的依存として環境に残り続ける。残っているかは `uv tree` で確認する。
- 上記の理由から、`import` が通ることは削除できた証拠にならない。`uv tree` に自分の直下の依存として現れないことを確認する。
- `--no-sync` を付けるとロックの更新だけを行い、環境からのアンインストールは行わない。通常は不要。

## 具体例：pytest（開発用依存）を追加する

テストツールのようにアプリの実行には不要なパッケージは、通常依存ではなく **`--dev` を付けて開発用依存グループに入れる**。`pyproject.toml` の `dependencies` を「アプリが動くのに必要なもの」だけに保てる。

1. コンテナを起動する。
   ```bash
   docker compose up -d backend
   ```
2. 開発用依存として追加する。`pyproject.toml` への追記と `uv.lock` の更新が同時に行われる。
   ```bash
   docker compose exec backend uv add --dev pytest
   ```
   `pyproject.toml` に以下が追記される（PEP 735 の `[dependency-groups]`）。
   ```toml
   [dependency-groups]
   dev = [
       "pytest>=9.1.1",
   ]
   ```
3. イメージを再ビルドする。コンテナも再作成される。
   ```bash
   docker compose up -d --build backend
   ```
4. インストールされたことを確認する。
   ```bash
   docker compose exec backend pytest --version
   # => pytest 9.1.1
   docker compose exec backend python -c "import pytest; print(pytest.__file__)"
   # => /usr/local/lib/python3.13/site-packages/pytest/__init__.py
   ```
   パスが `/usr/local/...` であればイメージ層に定着している。
5. `pyproject.toml` と `uv.lock` をコミットする。
