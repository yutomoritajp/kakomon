import { MainButton } from '../components/Button'

const summaries = [
  { id: 1, exam_period: "令和5年秋季", exam_section: "午前Ⅱ", quiz_number: "問10", result: "正解"},
  { id: 2, exam_period: "令和7年秋季", exam_section: "午前Ⅱ", quiz_number: "問14", result: "不正解"}
]

const Summary = () => {
    return (
      <>
        <h2 className="text-2xl font-yuji underline">解答終了</h2>
        <h3 className="text-xl font-yuji m-8">10問中8問正解（正答率80%）</h3>
        <table className="mx-auto font-yuji text-center text-xl border-collapse">
          <tr className="bg-point text-mainbase">
            <th className="border border-point px-10 py-3">項番</th>
            <th className="border border-point px-10 py-3">試験回</th>
            <th className="border border-point px-10 py-3">試験区分</th>
            <th className="border border-point px-10 py-3">問題番号</th>
            <th className="border border-point px-10 py-3">結果</th>
          </tr>
          { summaries.map(summary => (
            <tr>
              <td className="border border-main px-10 py-3">{ summary.id }</td>
              <td className="border border-main px-10 py-3">{ summary.exam_period }</td>
              <td className="border border-main px-10 py-3">{ summary.exam_section }</td>
              <td className="border border-main px-10 py-3">{ summary.quiz_number }</td>
              <td className="border border-main px-10 py-3">{ summary.result }</td>
            </tr>
          )) }
        </table>
        <MainButton>終了する</MainButton>
      </>
    )
}

export default Summary