import React, { useState, useEffect } from 'react';
import { Input, Button } from "reactstrap";
import Axios from 'axios';

const Bangalore = (props) => {
    const [data, setData] = useState({location: []});
    const [location, setLocation] = useState("");
    const [bhk, setBhk] = useState("");
    const [sqft, setSqft] = useState("");
    const [bath, setBath] = useState("");
    const [balcony, setBalcony] = useState("");
    useEffect(() => {
        Axios.get('http://localhost:5000/data/bangalore')
        .then
        (result => {
            setData(result.data)
        })
        .catch(error => {
            alert(error.message);
        })
    }, []);
    return (
        <div>
            <Input type="select" placeholder="locality" value={location} onChange={e => setLocation(e.target.value)}>
                {data.location.map(location => {
                    return (
                        <option label={location} value={location} key={location} />
                    )
                })}
            </Input>
            <Input type="number" placeholder="Square Feet" min={0} step={100} value={sqft} onChange={e => setSqft(e.target.value)} />
            <Input type="number" placeholder="BHK" min={1} step={1} value={bhk} onChange={e => setBhk(e.target.value)} />
            <Input type="number" placeholder="Baths" min={0} step={1} value={bath} onChange={e => setBath(e.target.value)} />
            <Input type="number" placeholder="Balconies" min={0} step={1} value={balcony} onChange={e => setBalcony(e.target.value)} />
            <Button color={'primary'} 
                onClick={() => {
                    Axios.post('http://localhost:5000/predict/bangalore', {
                        location,
                        bhk,
                        sqft,
                        bath,
                        balcony
                    })
                        .then(result => {
                            alert('Price: ' + result.data.price)
                        })
                        .catch(error => {
                            alert('Failed: \n' + error.message)
                        })
                }}
                title={'Predict'}
            > Predict </Button>
       </div>
    )
}

export default Bangalore;
