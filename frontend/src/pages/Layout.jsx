import { Outlet } from 'react-router'
import Header from '../components/Header'
import Footer from '../components/Footer'

const Layout = () => {
    return (
        <>
          <Header />
            <main>
              <div className='py-12 bg-subbase'>
                <div className='w-[clamp(64rem,90%,112rem)] mx-auto bg-mainbase rounded-md'>
                  <Outlet />
                </div>
              </div>
            </main>
          <Footer />
        </>
    )
}

export default Layout