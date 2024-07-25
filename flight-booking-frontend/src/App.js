import React from 'react';
import PlaneList from './components/PlaneList';
import TicketList from './components/TicketList';
import AeroportList from './components/AeroportList';
import CityList from './components/CityList';
import PassengerList from './components/PassengerList';


function App() {
  return (
    <div className="App">
      <h1>Flight Booking System</h1>
      <PlaneList />
      <AeroportList />
      <CityList />
      <TicketList />
      <PassengerList />
    </div>
  );
}

export default App;
