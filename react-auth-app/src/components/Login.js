import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { motion } from 'framer-motion';
import './Form.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [mobile, setMobile] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5001/Authentication/login', {
        email,
        mobile,
      });
      localStorage.setItem('token', response.data.data.token);
      toast.success('Logged-In successfully!');
      navigate('/welcome', { state: { name: response.data.data.name } });
    } catch (error) {
      toast.error('Login failed');
    }
  };

  return (
    <motion.div 
      className="form-container"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2>Login</h2>
      <motion.form 
        onSubmit={handleLogin} 
        className="form-box"
        initial={{ y: 50 }}
        animate={{ y: 0 }}
        transition={{ type: 'spring', stiffness: 100 }}
      >
        <motion.input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
          whileFocus={{ scale: 1.05 }}
        />
        <motion.input
          type="text"
          value={mobile}
          onChange={(e) => setMobile(e.target.value)}
          placeholder="Mobile"
          required
          whileFocus={{ scale: 1.05 }}
        />
        <motion.button 
          type="submit"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          Login
        </motion.button>
      </motion.form>
      <p>
        New to the app? <a href="/signup">Create User</a>
      </p>
    </motion.div>
  );
};

export default Login;
