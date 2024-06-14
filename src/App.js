import React from 'react';
import { Container, AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CreateTicket from './components/CreateTicket';
import GetTicketPage from './components/GetTicketPage';
import UpdateTicketPrice from './components/UpdateTicketPrice';
import ValidateTicket from './components/ValidateTicket';
import DeleteTicket from './components/DeleteTicket';

const App = () => {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1 }}>
            Ticket Management
          </Typography>
          <Button color="inherit" component={Link} to="/">
            Create Ticket
          </Button>
          <Button color="inherit" component={Link} to="/get-tickets">
            Get Tickets
          </Button>
          <Button color="inherit" component={Link} to="/update-price">
            Update Ticket Price
          </Button>
          <Button color="inherit" component={Link} to="/validate-ticket">
            Validate Ticket
          </Button>
          <Button color="inherit" component={Link} to="/delete-ticket">
            Delete Ticket
          </Button>
        </Toolbar>
      </AppBar>
      <Container>
        <Box mt={4}>
          <Routes>
            <Route path="/" element={<CreateTicket />} />
            <Route path="/get-tickets" element={<GetTicketPage />} /> 
            <Route path="/update-price" element={<UpdateTicketPrice />} />
            <Route path="/validate-ticket" element={<ValidateTicket />} />
            <Route path="/delete-ticket" element={<DeleteTicket />} />
          </Routes>
        </Box>
      </Container>
    </Router>
  );
};

export default App;
