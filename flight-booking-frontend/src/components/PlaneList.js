import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PlaneList = () => {
  const [planes, setPlanes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("Fetching planes...");
    axios.get('http://127.0.0.1:8000/api/plane/list/')
      .then(response => {
        console.log("Response data:", response.data);

        // Проверка типа данных и установка состояния
        if (Array.isArray(response.data)) {
          setPlanes(response.data);
        } else if (response.data.results && Array.isArray(response.data.results)) {
          setPlanes(response.data.results);
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
      <h2>Planes</h2>
      <ul>
        {planes.map(plane => (
          <li key={plane.id}>{plane.plane}</li>
        ))}
      </ul>
    </div>
  );
};

export default PlaneList;
