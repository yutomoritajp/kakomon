# Batch実行手順

`batch/`配下には、管理者がコンテナに入って手動実行するCLIスクリプトを配置する。
各スクリプトは薄いエントリポイントとし、実処理は`services/`配下のクラスに委譲する。

## 共通の実行方法

すべてのbatchは以下の形式でコンテナ内から実行する。

```
docker compose exec backend python -m batch.{モジュール名} [オプション...]
```

補足
- `-m`オプションでの実行が必須。`batch/`配下のスクリプトは`services`パッケージを絶対importしているため、`python batch/xxx.py`のようにファイルパス指定で直接実行すると`ModuleNotFoundError`になる。
- 各batchが受け取るオプション（必須引数・選択肢）は個別スクリプトの`--help`で確認できる。
  ```
  docker compose exec backend python -m batch.{モジュール名} --help
  ```

## 各batchの説明

### confirm_question_pdf

指定した試験回・試験区分・ページ範囲で、問題PDF(`question.pdf`)を範囲抽出し`temp/`配下に一時保存する。問題データ作成前に、対象ページ範囲が正しいかを目視確認する用途で使う。

```
docker compose exec backend python -m batch.confirm_question_pdf --period {試験回} --section {試験区分} --start {開始ページ} --end {終了ページ}
```

| オプション | 必須 | 内容 |
| --- | --- | --- |
| `--period` | ○ | 試験回（例: `r7`）。指定可能な値は`services/constants/period.py`を参照 |
| `--section` | ○ | 試験区分（例: `am1`）。指定可能な値は`services/constants/section.py`を参照 |
| `--start` | ○ | 抽出開始ページ（1始まり） |
| `--end` | ○ | 抽出終了ページ |

実行例
```
docker compose exec backend python -m batch.confirm_question_pdf --period r7 --section am1 --start 2 --end 10
```

出力されたPDFは`temp/p{start}-p{end}_{period}_{section}_question.pdf`として保存される。
