import SorryBot from '../assets/sorry_bot.svg'
import { MainButton } from '../components/Button'
import { BUTTON } from '../constants/message'
import { ROUTE } from '../constants/route'

const message = {
  statusCode: '500',
  title: '内部サーバーエラー',
  message: '申し訳ありません。サーバーで予期しないエラーが発生しました。時間をおいてもう一度画面を読み込んでください。'
}

const Error = () => {
    return (
      <div className="flex flex-col items-center">
        <h2 className="text-3xl font-yuji my-4"><span className="mr-8">{ message.statusCode }</span>{ message.title }</h2>
        <img src={ SorryBot } />
        <p className="mt-10 text-xl font-yuji text-center">{ message.message }</p>
        <MainButton to={ROUTE.TOP}>{ BUTTON.TO_TOP }</MainButton>
      </div>
    )
}

export default Error