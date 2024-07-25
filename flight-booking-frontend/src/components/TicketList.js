import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TicketList = () => {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("Fetching planes...");
    axios.get('http://127.0.0.1:8000/api/ticket/list/')
      .then(response => {
        console.log("Response data:", response.data);

        // Проверка типа данных и установка состояния
        if (Array.isArray(response.data)) {
          setTickets(response.data);
        } else if (response.data.results && Array.isArray(response.data.results)) {
          setTickets(response.data.results);
        } else {
          setError(new Error('Expected an array but received a different type'));
        }

        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the planes!', error);
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>
      <h2>Tickets</h2>
      <ul>
        {tickets.map(ticket => (
          <li key={ticket.id}>{ticket.ticket}</li>
        ))}
      </ul>
    </div>
  );
};

export default TicketList;
