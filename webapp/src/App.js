import React, { useState, useEffect } from 'react';
import './App.css';
import Bangalore from './Bangalore';
import Mumbai from './Mumbai';
import Chennai from './Chennai';
import Delhi from './Delhi';

const CityBox = (props) => {
  const {city} = props;
  switch (city) {
    case 'bangalore':
      return <Bangalore />
    case 'mumbai':
      return <Mumbai />
    case 'delhi':
      return <Delhi />
    case 'chennai':
      return <Chennai />
    default:
      return <Bangalore />
  }
}
function App() {
  const [city, setCity] = useState('bangalore')
  return (
    <div>
      <select name="City" value={city} onChange={e => {setCity(e.target.value)}}>
        <option value="bangalore" label="Bangalore" />
        <option value="mumbai" label="Mumbai" />
        <option value="delhi" label="Delhi" />
        <option value="chennai" label="Chennai" />
      </select>
      <CityBox city={city} />
    </div>
  );
}

export default App;
