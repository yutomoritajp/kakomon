import Correct from '../assets/correct.svg'
import Wrong from '../assets/wrong.svg'

const ResultIcon = ({ isCorrect }) => {
    const src = isCorrect ? Correct : Wrong;
    return (
        <img src={ src }
             alt=""
             className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
                animate-fadeout pointer-events-none"/>
    )
}

export default ResultIcon