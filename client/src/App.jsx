import React, { useState } from 'react'
import './App.css'
import Navbar from './Navbar'
import Footer from './Footer'
import { Route, Routes, useNavigate } from 'react-router'
import Login from './pages/Login'
import Signup from './pages/Signup'
import Feed from './pages/Feed'
import Explore from './pages/Explore'
import Profile from './pages/Profile'
import PostDetail from './pages/PostDetail'

function App() {
  const [user, setUser] = useState(null) // store logged in user
  const navigate = useNavigate()

  const handleLogout = () => {
    setUser(null)
    navigate("/") // redirect to login
  }

  return (
    <div>
      <Navbar user={user} onLogout={handleLogout} />

      <Routes>
        <Route path='/' element={<Login setUser={setUser} />} />
        <Route path='/signup' element={<Signup setUser={setUser} />} />
        <Route path='/feed' element={<Feed user={user} />} />
        <Route path='/explore' element={<Explore user={user} />} />
        <Route path='/profile/:id' element={<Profile user={user} />} />
        <Route path='/post/:id' element={<PostDetail user={user} />} />
      </Routes>

      <Footer />
    </div>
  )
}

export default App
