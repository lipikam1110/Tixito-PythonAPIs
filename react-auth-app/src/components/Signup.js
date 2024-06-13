// src/components/Signup.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { motion } from 'framer-motion';
import './Form.css'; // Updated to import the common Form.css

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
    <motion.div
      className="form-container"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2>Signup</h2>
      <motion.form
        onSubmit={handleSignup}
        className="form-box"
        initial={{ y: 50 }}
        animate={{ y: 0 }}
        transition={{ type: 'spring', stiffness: 100 }}
      >
        <motion.input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name"
          required
          whileFocus={{ scale: 1.05 }}
        />
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
        <div className="checkbox-container">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={whatsappNotificationEnable}
              onChange={(e) => setWhatsappNotificationEnable(e.target.checked)}
            />
            <span className="whatsapp-label">Enable WhatsApp Notifications</span>
          </label>
        </div>
        <motion.button
          type="submit"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          Signup
        </motion.button>
      </motion.form>
    </motion.div>
  );
};

export default Signup;
