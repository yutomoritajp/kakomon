import Bot from '../assets/bot.svg'


export function MainButton({children}) {
    return (
        <button className='h-12 w-73 bg-point text-mainbase
        text-2xl font-yuji rounded-md shadow-md cursor-pointer'>
            {children}
        </button>
    )
}

export function AIButton() {
    return (
        <button className='flex items-center border px-2 gap-2 font-yuji rounded-md shadow-md cursor-pointer'>
            <img src={Bot} />
            AIに質問する
        </button>
    )
}