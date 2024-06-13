import React, { useState, useEffect } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { toast } from 'react-toastify';
import { motion } from 'framer-motion';
import './Nav.css';

const Nav = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [selected, setSelected] = useState(location.pathname);

  useEffect(() => {
    setSelected(location.pathname);
  }, [location.pathname]);

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

  const handleSelect = (path) => {
    setSelected(path);
  };

  return (
    <motion.nav className="nav-bar">
      <ul className="nav-list">
        <motion.li 
          className={`nav-item ${selected === '/login' ? 'selected' : ''}`}
          whileHover={{ scale: 1.1 }}
        >
          <Link to="/login" onClick={() => handleSelect('/login')}>Login</Link>
        </motion.li>
        <motion.li 
          className={`nav-item ${selected === '/signup' ? 'selected' : ''}`}
          whileHover={{ scale: 1.1 }}
        >
          <Link to="/signup" onClick={() => handleSelect('/signup')}>Signup</Link>
        </motion.li>
        <motion.li 
          className="nav-item"
          whileHover={{ scale: 1.1 }}
        >
          <motion.button 
            onClick={handleLogout} 
            className="logout-button"
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
          >
            Logout
          </motion.button>
        </motion.li>
      </ul>
    </motion.nav>
  );
};

export default Nav;
