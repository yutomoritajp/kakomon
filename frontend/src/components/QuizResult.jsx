import ResultIcon from '../components/ResultIcon'
import { MainButton, AIButton } from '../components/Button'

const QuizResult = ({ isCorrect, selectedKey, answerKey, explanation }) => {
    return (
        <>
          <div className="flex justify-between items-end mt-8">
            <div>
              <h2 className={`text-xl font-jp ${isCorrect ? "text-correct" : "text-wrong"}`}>
                { isCorrect ? "正解" : "不正解" }
              </h2>
              <h3 className="text-lg font-jp mt-2">あなたの解答： { selectedKey }</h3>
              <h3 className="text-lg font-jp mt-2">正解：{ answerKey }</h3>
              <h3 className="text-lg font-jp mt-2">解説：</h3>
            </div>
            <AIButton />
          </div>
          <p className="mt-4 px-4 py-6 rounded-md bg-subbase font-jp">
            { explanation }
          </p>
          <MainButton>次の問題</MainButton>
          <ResultIcon isCorrect={ isCorrect } />
        </>
    )
}

export default QuizResult