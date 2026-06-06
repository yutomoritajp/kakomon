import CorrectIcon from '../assets/correct.svg'
import WrongIcon from '../assets/wrong.svg'

export function Collect() {
    return (
        <img src={CorrectIcon}  />
    )
}

export function Wrong() {
    return (
        <img src={WrongIcon} />
    )
}