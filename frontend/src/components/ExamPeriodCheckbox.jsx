import CheckIcon from '../assets/check.svg'

/**
 * @param {object} props
 * @param { {id: number, text: string}} props.period 試験回詳細情報
 * @param { Set<number> } props.checkedIds 選択済み試験回Id
 * @param { (id: number) => void} props.togglePeriod
 */
const ExamPeriodCheckbox = ({ period, checkedIds, togglePeriod }) => {
    const isChecked = checkedIds.has(period.id);
    return (
        <label className={`flex items-center gap-1 border p-4 text-xl text-center font-yuji rounded-md shadow-md
                cursor-pointer ${!isChecked ? "opacity-30" : null}`}>
            <img src={CheckIcon} className={`${!isChecked ? "opacity-0" : null}`} />
            <input 
                type="checkbox"
                name="exam_period"
                className="appearance-none"
                value={ period.id }
                onChange={ () => togglePeriod(period.id) }
                checked
            />
            { period.text }
        </label>
    )
}

export default ExamPeriodCheckbox