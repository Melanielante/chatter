import React from 'react'
import './App.css'
import Navbar from './Navbar'
import Footer from './Footer'
import {Route, Routes} from 'react-router'
import Login from './pages/Login';
import Signup from './pages/Signup';
import Feed from './pages/Feed';
import Explore from './pages/Explore';
import Profile from './pages/Profile';
import PostDetail from './pages/PostDetail';


function App() {
  

  return (
    <div>
      <Navbar />

      <Routes>
        <Route path='/' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
        <Route path='/feed' element={<Feed />} />
        <Route path='/explore' element={<Explore />} />
        <Route path='/profile/:id' element={<Profile />} />
        <Route path='/post/:id' element={<PostDetail />} />

      </Routes>

      <Footer />
      
    </div>
  )
}

export default App
