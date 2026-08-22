# pytest の設定と実行方法

テストの配置規約は `.claude/rules/backend.md` の「テスト規約」を参照。

## 設定

`tool.pytest.ini_options`に以下の設定を追加する。

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
addopts = "--import-mode=importlib"
```

- `testpaths`: UTの既定の探索範囲。本プロジェクトでは`tests/`配下にのみUTを作成する。
- `pythonpath`: `sys.path`に追加するパス。`/app`配下のモジュールをUTで使用可能。
- `addopts`: テストコマンドに`--import-mode=importlib`を付与
- `--import-mode=importlib`: インポートモード。rootdir(本プロジェクトでは`/app`)からの相対パスでテストモジュールを特定するので、同名のテストファイルを作成可能。

## 実行方法

```bash
docker compose exec backend pytest
```

`.pytest_cache/` は pytest が自身の配下に `.gitignore` を自動生成するため、リポジトリの `.gitignore` への追記は不要。
