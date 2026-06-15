import ResultIcon from '../components/ResultIcon'
import { MainButton, AIButton } from '../components/Button'
import { CORRECT, WRONG, YOUR_ANSWER, EXPLANATION, BUTTON } from '../constants/message'
import { ROUTE } from '../constants/route'

const QuizResult = ({ isCorrect, selectedKey, answerKey, explanation }) => {
    return (
        <>
          <div className="flex justify-between items-end mt-8">
            <div>
              <h2 className={`text-xl font-jp ${isCorrect ? "text-correct" : "text-wrong"}`}>
                { isCorrect ? CORRECT : WRONG }
              </h2>
              <h3 className="text-lg font-jp mt-2">{ YOUR_ANSWER } : { selectedKey }</h3>
              <h3 className="text-lg font-jp mt-2">{ CORRECT } : { answerKey }</h3>
              <h3 className="text-lg font-jp mt-2">{ EXPLANATION } : </h3>
            </div>
            <AIButton />
          </div>
          <p className="mt-4 px-4 py-6 rounded-md bg-subbase font-jp">
            { explanation }
          </p>
          <MainButton to={ ROUTE.SUMMARY }>{ BUTTON.SHOW_RESULT }</MainButton>
          <ResultIcon isCorrect={ isCorrect } />
        </>
    )
}

export default QuizResult