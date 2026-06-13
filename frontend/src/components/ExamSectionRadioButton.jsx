import CheckIcon from '../assets/check.svg'

/**
 * @param { object } props
 * @param { {id: number, text: string}} props.section 試験区分詳細情報
 * @param { number | null } props.selectedId 選択中試験区分Id
 * @param { (id: number | null) => void } props.setSelectedId
 */
const ExamSectionRadioButton = ({ section, selectedId, setSelectedId }) => {
    const isSelected = section.id === selectedId
    return (
        <label className="inline-flex items-center text-xl font-yuji cursor-pointer mr-8">
            <div className="border w-6 h-6 rounded-md mr-2">
                { isSelected && <img src={ CheckIcon } /> }
            </div>
            <input 
                type="radio"
                className="appearance-none"
                name="exam_section"
                value={ section.id }
                onChange={ () =>  setSelectedId(section.id) }
            />
            { section.text }
        </label>
    )
}

export default ExamSectionRadioButton