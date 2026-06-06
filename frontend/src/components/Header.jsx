import DbIcon from '../assets/db.svg'
import { APP_TITLE, APP_SUB_TITLE, TOP } from '../constants/message.js'

const Header = () => {
    return (
        <header>
          <div className='bg-mainbase'>
            <div className='flex items-center gap-2 p-2'>
                <img src={DbIcon} />
                <p className='text-point font-kosugi'>{ APP_SUB_TITLE }</p>
            </div>
            <h1 className='text-main font-yuji text-4xl text-center'>{ APP_TITLE }</h1>
          </div>
          <div className='bg-point p-4'>
             <nav>
                <ul className='text-mainbase text-xl font-jp'>
                    <li className='ml-6'><a href="#">{ TOP }</a></li>
                </ul>
             </nav>
          </div>
        </header>
    )
}

export default Header