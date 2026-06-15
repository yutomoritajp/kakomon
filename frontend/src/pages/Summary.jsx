import { MainButton } from '../components/Button'
import { BUTTON, SUMMARY_TITLE, SUMMARY_TABLE, CORRECT } from '../constants/message'
import { ROUTE } from '../constants/route'

const summaries = [
  { id: 1, exam_period: "令和5年秋季", exam_section: "午前Ⅱ", quiz_number: "問10", result: "正解"},
  { id: 2, exam_period: "令和7年秋季", exam_section: "午前Ⅱ", quiz_number: "問14", result: "不正解"}
]

const totalQuizCount = summaries.length;
const correctQuizCount = summaries.filter(summary => summary.result === CORRECT).length;

const getAccuracy = () => {
  return correctQuizCount * 100 / totalQuizCount
}

const Summary = () => {
    return (
      <>
        <h2 className="text-2xl font-yuji underline">{ SUMMARY_TITLE }</h2>
        <h3 className="text-xl font-yuji m-8">{`${totalQuizCount}問中${correctQuizCount}問正解（正答率${getAccuracy()}%）`}</h3>
        <table className="mx-auto font-yuji text-center text-xl border-collapse">
          <thead>
            <tr className="bg-point text-mainbase">
              <th className="border border-point px-10 py-3">{ SUMMARY_TABLE.INDEX }</th>
              <th className="border border-point px-10 py-3">{ SUMMARY_TABLE.EXAM_PERIOD }</th>
              <th className="border border-point px-10 py-3">{ SUMMARY_TABLE.EXAM_SECTION }</th>
              <th className="border border-point px-10 py-3">{ SUMMARY_TABLE.QUIZ_NUMBER }</th>
              <th className="border border-point px-10 py-3">{ SUMMARY_TABLE.RESULT }</th>
            </tr>
          </thead>
          <tbody>
            { summaries.map(summary => (
              <tr key={ summary.id }>
                <td className="border border-main px-10 py-3">{ summary.id }</td>
                <td className="border border-main px-10 py-3">{ summary.exam_period }</td>
                <td className="border border-main px-10 py-3">{ summary.exam_section }</td>
                <td className="border border-main px-10 py-3">{ summary.quiz_number }</td>
                <td className="border border-main px-10 py-3">{ summary.result }</td>
              </tr>
            ))}
          </tbody>
        </table>
        <MainButton to={ ROUTE.TOP }>{ BUTTON.FINISH }</MainButton>
      </>
    )
}

export default Summary