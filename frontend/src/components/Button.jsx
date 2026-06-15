import { Link } from 'react-router'
import Bot from '../assets/bot.svg'
import { BUTTON } from '../constants/message'


export function MainButton({ children, to }) {
    return (
        <Link
            to={ to }
            className="flex items-center justify-center h-12 w-73 bg-point text-mainbase mt-16 mx-auto block
                text-2xl font-yuji rounded-md shadow-md cursor-pointer">
            { children }
        </Link>
    )
}

export function AIButton() {
    return (
        <button className="flex items-center border px-2 gap-2 font-yuji rounded-md shadow-md">
            <img src={Bot} />
            { BUTTON.ASK_AI }
        </button>
    )
}