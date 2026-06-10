import { useState } from 'react'
import { Routes, Route} from 'react-router'
import Layout from '../src/pages/Layout'
import Top from '../src/pages/Top'
import Quiz from '../src/pages/Quiz'
import Summary from '../src/pages/Summary'
import Error from '../src/pages/Error'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Top />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/summary" element={<Summary />} />
        <Route path="*" element={<Error />} />
      </Route>
    </Routes>
  )
}

export default App
