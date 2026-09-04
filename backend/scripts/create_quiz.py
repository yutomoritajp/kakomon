import argparse

from constants.period import Period
from constants.section import Section
from scripts.setup_logging import setup_logging
from usecases.create_quiz import CreateQuiz
from values.page_range import PageRange


def main() -> None:
    """
    試験年度と試験区分、ページ範囲を受け取り、問題データを作成する。（QuizテーブルにInsertする）
    正しい試験年度、試験区分、ページ範囲を渡せているかはconfirm_question_pdfで確認する。
    """
    ## ログ設定
    setup_logging()

    parser = argparse.ArgumentParser(
        description="指定された試験年度と試験区分の問題データを作成します。"
    )
    parser.add_argument(
        "--period", dest="period", required=True, choices=[p.value for p in Period]
    )
    parser.add_argument(
        "--section", dest="section", required=True, choices=[s.value for s in Section]
    )
    parser.add_argument("--start", dest="start", required=True, type=int)
    parser.add_argument("--end", dest="end", required=True, type=int)

    args = parser.parse_args()

    draft_quizzes = CreateQuiz(Period(args.period), Section(args.section)).execute(
        PageRange(args.start, args.end)
    )

    if not draft_quizzes:
        print("Quizの作成に成功しました。画像配置が必要な問題はありません。")
    else:
        print(
            "Quizの作成に成功しました。画像配置が必要な問題は"
            + "、".join(f"第{num}問" for num in draft_quizzes)
            + "です。"
        )


if __name__ == "__main__":
    main()
