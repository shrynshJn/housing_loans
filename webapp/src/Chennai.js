import React, { useState, useEffect } from 'react';
import { Input, Button } from "reactstrap";
import Axios from 'axios';

const Bangalore = (props) => {
    const [data, setData] = useState({location: [], types: []});
    const [location, setLocation] = useState("");
    const [bhk, setBhk] = useState("");
    const [sqft, setSqft] = useState("");
    const [types, setType] = useState("");
    const [bath, setBath] = useState("");
    useEffect(() => {
        Axios.get('http://localhost:5000/data/chennai')
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
            <Input type="select" placeholder="Types" value={types} onChange={e => setType(e.target.value)}>
                {data.types.map(types => {
                    return (
                        <option label={types} value={types} key={types} />
                    )
                })}
            </Input>
            <Input type="number" placeholder="BHK" min={1} step={1} value={bhk} onChange={e => setBhk(e.target.value)} />
            <Input type="number" placeholder="Baths" min={0} step={1} value={bath} onChange={e => setBath(e.target.value)} />
            
            <Button color={'primary'} 
                onClick={() => {
                    Axios.post('http://localhost:5000/predict/chennai', {
                        location,
                        bhk,
                        sqft,
                        bath,
                        types,
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
