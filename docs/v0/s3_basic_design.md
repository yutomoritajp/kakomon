# 概要

`v0.requirements.md`に記載されているスコープのうち、`3. データ作成`を実施する。

## スコープ完了定義

データベーススペシャリスト試験(DB)の令和7年度(秋)の午前Ⅰの過去問の表示に必要なデータをDB及びストレージに入れる。

## 設計

### 過去問データの作成方法について

`quizzes`テーブルに格納する`number`, `content`, `correct_option`はbatch処理 + LLM APIで作成する。
成果物として`exams`テーブルと`quizzes`テーブルにデータが格納されるシーディングファイルが作成される。

#### 大まかな処理の流れと責務

1. 元データとなるpdfファイルをストレージから取得する。（batch処理）
2. pdfから必要な情報を切り出し、APIを呼ぶ。(batch処理)
3. 問題文のテキストを受け取り、成形して返す。（LLM API）
   ※LLMへの入力形式（テキストのみ / 画像同梱 / PDF同梱）は精度に依存するため実装時に検証して決定する。
4. 画像をストレージに保存する。（batch処理）

```mermaid
---
title: 処理イメージ(Todo:実装が確定したらこの図を実装に合わせて修正する)
---
sequenceDiagram
participant User
participant Batch
participant Storage
participant Api

User ->> Batch: period_code, section_code
Batch ->> Storage: period_code, section_code
Storage -->> Batch: question.pdf, answer.pdf
loop 問題数分ループする
Batch ->> Batch: 問題ごとにpdfを分割し問題部全体を画像に変換
Batch ->> Batch: 文字列はテキスト化/表・図は画像変換
Batch ->> Api: 全体画像/文字列/図・表の画像
Api ->> Api: 全体画像から整形されたマークダウンを作成
Api -->> Batch: 問題部text
end
Batch ->> Batch: シーディングファイル作成
Batch -->> User: 完了通知

```


#### 元データの格納場所について

過去問のpdfファイルは以下のように格納しておく。

```
.
├── backend/
    ├── data/
        ├── past_exams
            ├── r7
            |   ├── am1
            |   |   ├── question.pdf
            |   |   └── answer.pdf
            |   ├── am2
            |   
            ├── r6
```

#### 画像データ保存場所について

問題文及び選択肢が「図」や「グラフ」だった場合、画像データとして保持する必要がある。どのような画像をどのように保存するかについて記載する。

画像データは、「試験回」/ 「試験区分」/ 「カテゴリー」(「問題部」(question)、「解説部」(commentary)) / 問題番号で分類するものとする。
平積みにせず分類分けするのは、不都合な画像データができたとき人の目による確認が必要そうであるから、人が確認しやすい形式にするため。

```
.
├── backend/
    ├── data/
        ├── storage/
            ├── r7/
            |   ├── am1/
            |   |   ├── questions/
            |   |   |   ├── 3/
            |   |   |       ├── 1.png
            |   |   |       └── 2.png
            |   |   ├── commentaries/
            |   |       ├── 1/
            |   |           └── 1.png
            |   ├── am2/
            ├── r6/
            ├── r5/
```

画像データはpngとする。（1問あたり画像ファイルは10枚未満になる想定。）
画像ファイル名は、その問題・解説に出てくる順番で命名する。（1つ目の画像なら、`1.png`）

※Markdown形式のデータ(`quizzes.content`など)に画像参照パスを埋め込むものことを想定。

## 対応手順（目安）

1. 画像データの保存場所を決める。
2. 1問問題データを作ってみて、画面上で表示してみる。
3. 複数問題を効率よく作成する方法を考える（ClaudeのSkillを使うとかかな？）
4. 令和7年度(秋)の午前Ⅰの問題データをすべて作る。