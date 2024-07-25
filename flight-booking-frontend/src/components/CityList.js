import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CityList = () => {
  const [cities, setCities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("Fetching planes...");
    axios.get('http://127.0.0.1:8000/api/city/list/')
      .then(response => {
        console.log("Response data:", response.data);

        // Проверка типа данных и установка состояния
        if (Array.isArray(response.data)) {
          setCities(response.data);
        } else if (response.data.results && Array.isArray(response.data.results)) {
          setCities(response.data.results);
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
      <h2>Cities</h2>
      <ul>
        {cities.map(city => (
          <li key={city.id}>{city.city}</li>
        ))}
      </ul>
    </div>
  );
};

export default CityList;
