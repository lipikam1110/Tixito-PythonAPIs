// src/components/Signup.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import './Form.css';  // Updated to import the common Form.css

const Signup = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [mobile, setMobile] = useState('');
  const [whatsappNotificationEnable, setWhatsappNotificationEnable] = useState(false);
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5001/Authentication/signup', {
        name,
        email,
        mobile,
        whatsappNotificationEnable,
      });
      localStorage.setItem('token', response.data.data.token);
      toast.success('User created successfully!');
      navigate('/login');
    } catch (error) {
      if (error.response && error.response.data && error.response.data.message) {
        toast.error(error.response.data.message);
      } else {
        toast.error('Signup failed');
      }
    }
  };

  return (
    <div className="form-container">
      <h2>Signup</h2>
      <form onSubmit={handleSignup} className="form-box">
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name"
          required
        />
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
        <label>
          <input
            type="checkbox"
            checked={whatsappNotificationEnable}
            onChange={(e) => setWhatsappNotificationEnable(e.target.checked)}
          />
          Enable WhatsApp Notifications
        </label>
        <button type="submit">Signup</button>
      </form>
    </div>
  );
};

export default Signup;
