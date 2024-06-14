import React, { useState, forwardRef } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Typography, Grid, Snackbar } from '@mui/material';
import MuiAlert from '@mui/material/Alert';

const Alert = forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const ValidateTicket = () => {
  const [ticketId, setTicketId] = useState('');
  const [validatedOn, setValidatedOn] = useState('');
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');
  const [snackbarMessage, setSnackbarMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.patch(`http://localhost:5000/tickets/${ticketId}/validate`, { validatedOn });
      setSnackbarSeverity('success');
      setSnackbarMessage('Ticket validated successfully!');
      setSnackbarOpen(true);
    } catch (error) {
      setSnackbarSeverity('error');
      setSnackbarMessage(error.response ? error.response.data.error : 'Error validating ticket!');
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
        Validate Ticket
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
              type="date"
              name="validatedOn"
              label="Validated On"
              fullWidth
              value={validatedOn}
              onChange={(e) => setValidatedOn(e.target.value)}
              InputLabelProps={{
                shrink: true,
              }}
            />
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Validate Ticket
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
    </Container>
  );
};

export default ValidateTicket;
