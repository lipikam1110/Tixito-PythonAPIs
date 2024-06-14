import React, { useState, forwardRef } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Typography, Grid, Snackbar, Paper } from '@mui/material';
import MuiAlert from '@mui/material/Alert';

const Alert = forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const UpdateTicketPrice = () => {
  const [ticketId, setTicketId] = useState('');
  const [price, setPrice] = useState('');
  const [oldPrice, setOldPrice] = useState('');
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');
  const [snackbarMessage, setSnackbarMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Fetch the current price
      const response = await axios.get(`http://localhost:5000/tickets/${ticketId}`);
      const currentPrice = response.data.sellingPrice;
      setOldPrice(currentPrice);

      // Update the price
      await axios.patch(`http://localhost:5000/tickets/${ticketId}/price`, { sellingPrice: price });
      setSnackbarSeverity('success');
      setSnackbarMessage(`Ticket price updated successfully to ${price}!`);
      setSnackbarOpen(true);
    } catch (error) {
      setSnackbarSeverity('error');
      setSnackbarMessage(error.response ? error.response.data.error : 'Error updating ticket price!');
      setSnackbarOpen(true);
    }
  };

  const handleSnackbarClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setSnackbarOpen(false);
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Update Ticket Price
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <TextField
              type="text"
              name="ticketId"
              label="Ticket ID"
              fullWidth
              value={ticketId}
              onChange={(e) => setTicketId(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              type="text"
              name="price"
              label="New Price"
              fullWidth
              value={price}
              onChange={(e) => setPrice(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Update Price
            </Button>
          </Grid>
        </Grid>
      </form>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={handleSnackbarClose}
      >
        <Alert onClose={handleSnackbarClose} severity={snackbarSeverity}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
      {oldPrice && (
        <Paper style={{ padding: 20, marginTop: 20 }}>
          <Typography variant="h6" gutterBottom>
            Price updated from {oldPrice} to {price}
          </Typography>
        </Paper>
      )}
    </Container>
  );
};

export default UpdateTicketPrice;
