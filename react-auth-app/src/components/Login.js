// src/components/Login.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import './Form.css';  // Updated to import the common Form.css

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
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin} className="form-box">
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <input
          type="text"
          value={mobile}
          onChange={(e) => setMobile(e.target.value)}
          placeholder="Mobile"
          required
        />
        <button type="submit">Login</button>
      </form>
      <p>
        New to the app? <a href="/signup">Create User</a>
      </p>
    </div>
  );
};

export default Login;
