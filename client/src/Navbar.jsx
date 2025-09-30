import React from "react";
import { NavLink } from "react-router";
import "./App.css";

function Navbar({ user, onLogout }) {
  return (
    <nav className="navbar">
      <h2 className="logo">Chatter</h2>

      <ul className="nav-links">
        {user ? (
          <>
            <li>
              <NavLink
                to="/feed"
                className={({ isActive }) => (isActive ? "active" : "")}
              >
                Feed
              </NavLink>
            </li>
            <li>
              <NavLink
                to="/explore"
                className={({ isActive }) => (isActive ? "active" : "")}
              >
                Explore
              </NavLink>
            </li>
            <li>
              <NavLink
                to={`/profile/${user.id}`}
                className={({ isActive }) => (isActive ? "active" : "")}
              >
                Profile
              </NavLink>
            </li>
            <li>
              <button onClick={onLogout} className="logout-btn">
                Logout
              </button>
            </li>
          </>
        ) : (
          <>
            <li>
              <NavLink
                to="/"
                className={({ isActive }) => (isActive ? "active" : "")}
              >
                Login
              </NavLink>
            </li>
            <li>
              <NavLink
                to="/signup"
                className={({ isActive }) => (isActive ? "active" : "")}
              >
                Signup
              </NavLink>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
