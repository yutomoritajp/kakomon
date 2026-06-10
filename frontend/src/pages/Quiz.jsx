import { useState } from 'react'
import AnswerOption from '../components/AnswerOption'
import QuizResult from '../components/QuizResult'

const quiz = {
    options: [
        { "key": "ア", "text": "算術演算によって得られた属性の組である" },
        { "key": "イ", "text": "実票を冗長にして利用しやすくする" },
        { "key": "ウ", "text": "導出表は名前を持つことができない" },
        { "key": "エ", "text": "ビューは導出表の一つの形態である" }
    ],
    answerKey: "エ",
    explanation : "ここに解説が入ります。ここに解説が入ります。"
}

const Quiz = () => {
    const [selectedKey, setSelectedKey] = useState(null);
    const isCorrect = selectedKey === quiz.answerKey;

    return (
      <>
        <div className="flex justify-between items-end">
          <div>
            <h2 className="text-2xl font-yuji underline">データベーススペシャリスト試験過去問</h2>
            <h3 className="text-xl font-jp font-bold mt-8">第一問</h3>
            <p className="text-lg font-jp mt-4 mb-8">導出表に関する記述として適切なものはどれか。</p>
            {quiz.options.map(option => (
              <AnswerOption
                key={ option.key }
                option={ option }
                answerKey={ quiz.answerKey }
                selectedKey={ selectedKey }
                onSelect={ setSelectedKey }
              />
            ))}
          </div>
          <div className="text-right font-yuji">
            <h3 className="text-lg">平成30年春季<span className="ml-4">問12</span></h3>
            <p>1問目 / 10問中</p>
          </div>
        </div>
        { selectedKey !== null &&
          <QuizResult
            isCorrect={ isCorrect }
            selectedKey={ selectedKey }
            answerKey={ quiz.answerKey }
            explanation={ quiz.explanation }
          />
        }
      </>
    )
}

export default Quiz