
const AnswerOption = ({ option, selectedKey, answerKey, onSelect }) => {
    const isAnswering = selectedKey === null;

    const buttonClass = isAnswering ? "cursor-pointer hover:bg-point hover:text-mainbase"
                      : option.key === answerKey ? "text-mainbase bg-correct"
                      : selectedKey === option.key ? "text-mainbase bg-wrong" 
                      : null;

    return (
        <div className="mb-4">
            <label className={`flex items-center gap-2 font-jp ${isAnswering ? "cursor-pointer" : null}`}>
                <button 
                    type="button"
                    onClick = {() => onSelect(option.key)}
                    className={`border h-8 w-8 rounded-lg ${buttonClass}`}
                    disabled={ !isAnswering }>
                    { option.key }
                </button>
                <span className="text-lg">{ option.text }</span>
            </label>
        </div>
    )

}

export default AnswerOption