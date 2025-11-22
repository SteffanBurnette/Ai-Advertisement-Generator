import React from 'react'
import {Routes, Route} from 'react-router'
import LandingPage from './pages/LandingPage.jsx'
import HomePage from './pages/HomePage.jsx'
import AdvertDetailPage from './pages/AdvertDetailPage.jsx'
import CreateAdvertPage from './pages/CreateAdvertPage.jsx'
import toast from 'react-hot-toast'


const App = () => {
  return (
    <div>
    <Routes>
        <Route path = "/" element = {<LandingPage/>}/>
        <Route path = "/main" element = {<HomePage/>} />
        <Route path = "/create" element = {<CreateAdvertPage/>}/>
        <Route path = "/details/:id" element = {<AdvertDetailPage/>} />

    </Routes>

    </div>
  )
}

export default App

//Example of react-hot-toast
//<button onClick = {() => toast.success("Congrats")}>Click me</button>