import React, { useState } from 'react';
import axios from 'axios';
import { Container, Typography, TableContainer, Table, TableHead, TableBody, TableRow, TableCell, Paper, TextField, Button, Snackbar, Alert } from '@mui/material';

const GetTicketPage = () => {
  const [ticketId, setTicketId] = useState('');
  const [ticket, setTicket] = useState(null);
  const [loading, setLoading] = useState(false);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');

  const handleInputChange = (e) => {
    setTicketId(e.target.value);
  };

  const fetchTicketById = async () => {
    if (!ticketId) {
      alert('Please enter a ticket ID');
      return;
    }
    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:5000/tickets/${ticketId}`);
      const ticketData = response.data.data; // Access the data field
      setTicket(ticketData);
      setSnackbarMessage('Ticket fetched successfully');
      setSnackbarSeverity('success');
      setLoading(false);
    } catch (error) {
      console.error('Error fetching ticket:', error);
      setTicket(null);
      setSnackbarMessage('Error fetching ticket');
      setSnackbarSeverity('error');
      setLoading(false);
    }
    setSnackbarOpen(true);
  };

  const handleSnackbarClose = () => {
    setSnackbarOpen(false);
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Get Ticket by ID
      </Typography>
      <TextField
        label="Ticket ID"
        value={ticketId}
        onChange={handleInputChange}
        fullWidth
        margin="normal"
      />
      <Button variant="contained" color="primary" onClick={fetchTicketById}>
        Fetch Ticket
      </Button>
      {loading ? (
        <p>Loading...</p>
      ) : ticket ? (
        <TableContainer component={Paper} style={{ marginTop: 20 }}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Actual Price</TableCell>
                <TableCell>Comment</TableCell>
                <TableCell>Event Venues ID</TableCell>
                <TableCell>Image URL</TableCell>
                <TableCell>Listing Price</TableCell>
                <TableCell>Lock</TableCell>
                <TableCell>Orders ID</TableCell>
                <TableCell>Seller ID</TableCell>
                <TableCell>Selling Price</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Type</TableCell>
                <TableCell>Validated On</TableCell>
                <TableCell>Verified</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow key={ticket.id}>
                <TableCell>{ticket.id || 'N/A'}</TableCell>
                <TableCell>{ticket.actualPrice || 'N/A'}</TableCell>
                <TableCell>{ticket.comment || 'N/A'}</TableCell>
                <TableCell>{ticket.eventVenuesID || 'N/A'}</TableCell>
                <TableCell>{ticket.imageURL || 'N/A'}</TableCell>
                <TableCell>{ticket.listingPrice || 'N/A'}</TableCell>
                <TableCell>{ticket.lock?.toString() || 'N/A'}</TableCell>
                <TableCell>{ticket.ordersID || 'N/A'}</TableCell>
                <TableCell>{ticket.sellerID || 'N/A'}</TableCell>
                <TableCell>{ticket.sellingPrice || 'N/A'}</TableCell>
                <TableCell>{ticket.status || 'N/A'}</TableCell>
                <TableCell>{ticket.type || 'N/A'}</TableCell>
                <TableCell>{ticket.validatedOn || 'N/A'}</TableCell>
                <TableCell>{ticket.verified?.toString() || 'N/A'}</TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      ) : (
        <p>No ticket data available</p>
      )}
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

export default GetTicketPage;
