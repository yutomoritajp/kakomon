import SorryBot from '../assets/sorry_bot.svg'
import { MainButton } from '../components/Button'

const Error = () => {
    return (
      <div className="flex flex-col items-center">
        <h2 className="text-3xl font-yuji my-4"><span className="mr-8">500</span>内部サーバーエラー</h2>
        <img src={ SorryBot } />
        <p className="mt-10 text-xl font-yuji text-center">申し訳ありません。サーバーで予期しないエラーが発生しました。<br />時間をおいてもう一度画面を再読み込みしてください。</p>
        <MainButton>戻る</MainButton>
      </div>
    )
}

export default Error