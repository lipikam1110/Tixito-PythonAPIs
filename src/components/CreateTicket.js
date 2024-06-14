import React, { useState, forwardRef, useEffect } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Typography, Grid, FormControlLabel, Checkbox, Paper, Snackbar, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import MuiAlert from '@mui/material/Alert';

// ForwardRef for Alert component
const Alert = forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const CreateTicket = () => {
  const [ticket, setTicket] = useState({
    actualPrice: '',
    comment: '',
    eventVenuesID: '',
    imageURL: '',
    listingPrice: '',
    lock: false,
    ordersID: '',
    sellerID: '',
    sellingPrice: '',
    status: '',
    type: '',
    validatedOn: '',
    verified: false,
  });

  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [createdTicket, setCreatedTicket] = useState(null); // State to hold the created ticket
  const [fetchingTicket, setFetchingTicket] = useState(false); // State to manage fetching status
  const [ticketId, setTicketId] = useState(null); // State to hold the ID of the created ticket

  useEffect(() => {
    const fetchTicketById = async () => {
      if (ticketId) {
        try {
          setFetchingTicket(true);
          const response = await axios.get(`http://localhost:5000/tickets/${ticketId}`);
          setCreatedTicket(response.data.data); // Access the data field
          setFetchingTicket(false);
        } catch (error) {
          console.error(error);
          setSnackbarSeverity('error');
          setSnackbarMessage('Error fetching ticket!');
          setSnackbarOpen(true);
          setFetchingTicket(false);
        }
      }
    };

    fetchTicketById();
  }, [ticketId]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setTicket({ ...ticket, [name]: type === 'checkbox' ? checked : value });
  };

  const validateForm = () => {
    for (const key in ticket) {
      if (ticket[key] === '' || ticket[key] === null) {
        return false;
      }
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) {
      setSnackbarSeverity('error');
      setSnackbarMessage('Please fill all fields!');
      setSnackbarOpen(true);
      return;
    }
    try {
      const response = await axios.post('http://localhost:5000/tickets', ticket);
      console.log(response.data);
      setSnackbarSeverity('success');
      setSnackbarMessage('Ticket created successfully!');
      setTicketId(response.data.data.id); // Assuming the response data contains the created ticket's ID in 'data'
      setSnackbarOpen(true);
    } catch (error) {
      console.error(error);
      setSnackbarSeverity('error');
      setSnackbarMessage('Error creating ticket!');
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
      <Paper style={{ padding: 20 }}>
        <Typography variant="h4" gutterBottom>
          Create Ticket
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={3}>
            {Object.keys(ticket).map((key) => (
              <Grid item xs={12} key={key}>
                {key === 'lock' || key === 'verified' ? (
                  <FormControlLabel
                    control={<Checkbox checked={ticket[key]} onChange={handleChange} name={key} />}
                    label={key}
                  />
                ) : (
                  <TextField
                    type="text"
                    name={key}
                    label={key}
                    fullWidth
                    value={ticket[key]}
                    onChange={handleChange}
                    InputLabelProps={{ shrink: true }}
                  />
                )}
              </Grid>
            ))}
            <Grid item xs={12}>
              <Button type="submit" variant="contained" color="primary" fullWidth>
                Create Ticket
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={handleSnackbarClose}
      >
        <Alert onClose={handleSnackbarClose} severity={snackbarSeverity}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
      {fetchingTicket && <p>Loading ticket...</p>}
      {createdTicket && (
        <TableContainer component={Paper} style={{ marginTop: 20 }}>
          <Table>
            <TableHead>
              <TableRow>
                {Object.keys(createdTicket).map((key) => (
                  <TableCell key={key}>{key}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow>
                {Object.values(createdTicket).map((value, index) => (
                  <TableCell key={index}>{value?.toString()}</TableCell>
                ))}
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Container>
  );
};

export default CreateTicket;
