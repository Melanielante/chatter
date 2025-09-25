import React from "react";
import { NavLink } from "react-router";
// import "./Navbar.css"; 

function Navbar() {
  return (
    <nav className="navbar">
      <h2 className="logo">Chatter</h2>

      <ul className="nav-links">
        <li>
          <NavLink to="/feed" className={({ isActive }) => (isActive ? "active" : "")}>
            Feed
          </NavLink>
        </li>
        <li>
          <NavLink to="/explore" className={({ isActive }) => (isActive ? "active" : "")}>
            Explore
          </NavLink>
        </li>
        <li>
          <NavLink to="/profile/1" className={({ isActive }) => (isActive ? "active" : "")}>
            Profile
          </NavLink>
        </li>
        <li>
          <NavLink to="/" className={({ isActive }) => (isActive ? "active" : "")}>
            Login
          </NavLink>
        </li>
        <li>
          <NavLink to="/signup" className={({ isActive }) => (isActive ? "active" : "")}>
            Signup
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
