import React, { useState } from "react";
import "./App.css";
import Navbar from "./Navbar";
import Footer from "./Footer";
import { Route, Routes, Navigate, useNavigate } from "react-router";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Feed from "./pages/Feed";
import Explore from "./pages/Explore";
import Profile from "./pages/Profile";
import PostDetail from "./pages/PostDetail";

// helper wrapper for private routes
function ProtectedRoute({ user, children }) {
  if (!user) {
    return <Navigate to="/" replace />;
  }
  return children;
}

function App() {
  const [user, setUser] = useState(null); // store logged in user
  const navigate = useNavigate();

  const handleLogout = () => {
    setUser(null);
    navigate("/"); // redirect to login
  };

  return (
    <div>
      <Navbar user={user} onLogout={handleLogout} />

      <Routes>
        {/* Public routes */}
        <Route path="/" element={<Login setUser={setUser} />} />
        <Route path="/signup" element={<Signup setUser={setUser} />} />

        {/* Private routes */}
        <Route
          path="/feed"
          element={
            <ProtectedRoute user={user}>
              <Feed user={user} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/explore"
          element={
            <ProtectedRoute user={user}>
              <Explore user={user} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/profile/:id"
          element={
            <ProtectedRoute user={user}>
              <Profile user={user} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/post/:id"
          element={
            <ProtectedRoute user={user}>
              <PostDetail user={user} />
            </ProtectedRoute>
          }
        />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
