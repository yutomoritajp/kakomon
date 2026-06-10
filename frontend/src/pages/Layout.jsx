import { Outlet } from 'react-router'
import Header from '../components/Header'
import Footer from '../components/Footer'

const Layout = () => {
    return (
        <div className="min-h-screen flex flex-col">
          <Header />
            <main className="flex-1 bg-subbase">
              <div className="py-12">
                <div className="w-[clamp(64rem,90%,112rem)] mx-auto p-16 bg-mainbase rounded-md">
                  <Outlet />
                </div>
              </div>
            </main>
          <Footer />
        </div>
    )
}

export default Layout