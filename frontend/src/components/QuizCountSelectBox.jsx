import { HYPHEN } from '../constants/message'

/**
 * @param { object } props
 * @param { number[] } props.counts 問題数候補リスト
 * @param { (quizCount: number) => void } props.setCount
 */
const QuizCountSelectBox = ({ counts, setCount }) => {
    return (
        <>
          <select 
              className="border px-2 py-1 cursor-pointer"
              onChange={e => setCount(Number(e.target.value))}>
            { [0, ...counts].map(count => (
                <option 
                    key={ count }
                    value={ count }>{ count == 0 ? HYPHEN : count }</option>
            ))}
          </select>
        </>
    )
}

export default QuizCountSelectBox