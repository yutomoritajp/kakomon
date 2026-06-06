import { APP_TITLE } from '../constants/message.js'

const Footer = () => {
    return (
        <footer>
          <div className='flex justify-end items-end h-32 p-4 bg-point'>
            <p className='text-mainbase text-lg font-jp'>{ APP_TITLE }</p>
          </div>
        </footer>
    )
}

export default Footer