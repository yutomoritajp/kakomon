import { useState } from 'react'
import ExamPeriodCheckbox from '../components/ExamPeriodCheckbox'
import ExamSectionRadioButton from '../components/ExamSectionRadioButton'
import QuizCountSelectBox from '../components/QuizCountSelectBox'
import { MainButton } from '../components/Button'
import { BUTTON, SELECT_EXAM_PERIOD, SELECT_EXAM_SECTION } from '../constants/message'
import { ROUTE } from '../constants/route'

const periods = [
  { id: 1, text: "令和7年秋季" },
  { id: 2, text: "令和6年秋期" },
  { id: 3, text: "令和5年秋期" },
  { id: 4, text: "令和4年秋期" },
  { id: 5, text: "令和3年秋期" },
  { id: 6, text: "令和2年秋期" },
  { id: 7, text: "令和元年秋期" },
  { id: 8, text: "平成31年秋期" }
];

const sections = [
  { id: 1, text: "午前Ⅰ"},
  { id: 2, text: "午前Ⅱ"},
  { id: 3, text: "午後Ⅰ"},
  { id: 4, text: "午後Ⅱ"}
];

const quizCounts = [ 1, 3, 5, 10 ];

const Top = () => {
    const [checkedPeriods, setCheckedPeriods] = useState(new Set(periods.map(_ => _.id)));
    const [checkedSection, setCheckedSection] = useState(/** @type {number | null} */ (null));
    const [quizCount, setQuizCount] = useState(0);

    const togglePeriod = id => {
      setCheckedPeriods(prev => {
        const next = new Set(prev);
        next.has(id) ? next.delete(id) : next.add(id);
        return next;
      })
    }
    return (
      <>
        <div className="relative grid grid-cols-3 gap-x-8 gap-y-4 border p-8 rounded-md">
          <p className="absolute -top-4 left-4 text-xl font-yuji bg-mainbase">{ SELECT_EXAM_PERIOD }</p>
          { periods.map(period => (
            <ExamPeriodCheckbox 
                key={ period.id }
                period={ period }
                checkedIds={ checkedPeriods }
                togglePeriod={ togglePeriod }
            />
          )) }
        </div>
        <div className="relative my-16 border p-8 rounded-md">
          <p className="absolute -top-4 left-4 text-xl font-yuji bg-mainbase">{ SELECT_EXAM_SECTION }</p>
          { sections.map(section => (
            <ExamSectionRadioButton 
                key={ section.id }
                section={ section }
                selectedId={ checkedSection }
                setSelectedId={ setCheckedSection }
            />
          )) }
        </div>
        <div className="text-xl text-center font-yuji">
          <QuizCountSelectBox counts={ quizCounts } setCount={ setQuizCount } />
          <span className="mx-2">問</span>
        </div>
        <MainButton to={ ROUTE.QUIZ }>{ BUTTON.START }</MainButton>
      </>
    )
}

export default Top