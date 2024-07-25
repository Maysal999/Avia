import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AeroportList = () => {
  const [aeroports, setAeroports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("Fetching planes...");
    axios.get('http://127.0.0.1:8000/api/aeroport/list/')
      .then(response => {
        console.log("Response data:", response.data);

        // Проверка типа данных и установка состояния
        if (Array.isArray(response.data)) {
          setAeroports(response.data);
        } else if (response.data.results && Array.isArray(response.data.results)) {
          setAeroports(response.data.results);
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
      <h2>Aeroports</h2>
      <ul>
        {aeroports.map(aeroport => (
          <li key={aeroport.id}>{aeroport.aeroport}</li>
        ))}
      </ul>
    </div>
  );
};

export default AeroportList;
