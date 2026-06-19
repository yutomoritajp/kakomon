# 概要

`v0.requirements.md`に記載されているスコープのうち、`1. 画面遷移`を実施する。

## スコープ完了定義

後述する画面遷移図のうち、AIチャット機能以外の画面遷移ができること。
ただし、データのやり取りは実施しない。

## 設計

### 1. 画面遷移図

[Figma](https://www.figma.com/design/6A8vlOMTD2H2ANT5SbWHWE/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%82%B9%E3%83%9A%E3%82%B7%E3%83%A3%E3%83%AA%E3%82%B9%E3%83%88%E9%81%8E%E5%8E%BB%E5%95%8F%E5%95%8F%E7%AD%94?node-id=25-880)に記載。

AIに質問機能はスコープ外のため、「AIに質問する」ボタンは"disable"とする。

### 2. URL設計

| 画面名 | URL | コンポーネント名 | 補足 | 
| --- | --- | --- |
| 出題範囲選択画面 | / | Top | トップページを兼ねる |
| 出題画面 | /quiz | Quiz |  |
| 採点画面 | /quiz | 出題画面と同じページ（遷移しない） |
| 結果一覧画面 | /summary | Summary |
| エラー画面 | /error | Error  |


## 対応手順(目安)

1. React環境を作成
  - [こちら](https://zenn.dev/yutomoritajp/articles/87097a5be2012b)の記事を参考に、Docker×React環境を作成。
2. 画面作成（画面遷移できるようにする）