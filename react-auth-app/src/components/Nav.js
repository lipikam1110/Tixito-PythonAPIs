// src/components/Nav.js
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import './Nav.css';

const Nav = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    const token = localStorage.getItem('token');
    if (!token) {
      toast.error('Please Login First');
      return;
    }
    localStorage.removeItem('token');
    toast.success('Logged Out successfully!');
    navigate('/login');
  };

  return (
    <nav className="nav-bar">
      <ul className="nav-list">
        <li className="nav-item">
          <Link to="/login">Login</Link>
        </li>
        <li className="nav-item">
          <Link to="/signup">Signup</Link>
        </li>
        <li className="nav-item">
          <button onClick={handleLogout} className="logout-button">Logout</button>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
