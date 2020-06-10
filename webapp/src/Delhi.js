import React, { useState, useEffect } from 'react';
import { Input, Button, Label } from "reactstrap";
import Axios from 'axios';

const Mumbai = (props) => {
    const [data, setData] = useState({locality: [], furnished: [], types: [], status: [], transactions: []});
    const [bhk, setBhk] = useState("");
    const [locality, setLocality] = useState("");
    const [area, setArea] = useState("");
    const [bath, setBath] = useState("");
    const [furnished, setFurnished] = useState("");
    const [parking, setParking] = useState(true);
    const [status, setStatus] = useState("");
    const [transaction, setTransaction] = useState("");
    const [types, setType] = useState("");  
    
    useEffect(() => {
        Axios.get('http://localhost:5000/data/delhi')
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
            <Input type="select" placeholder="locality" value={locality} onChange={e => setLocality(e.target.value)}>
                {data.locality.map(locality => {
                    return (
                        <option label={locality} value={locality} key={locality} />
                    )
                })}
            </Input>
            <Input type="number" placeholder="BHK" min={1} step={1} value={bhk} onChange={e => setBhk(e.target.value)} />
            <Input type="number" placeholder="Area" min={0} step={100} value={area} onChange={e => setArea(e.target.value)} />
            <Input type="number" placeholder="Baths" min={0} step={1} value={bath} onChange={e => setBath(e.target.value)} />
            <Input type="select" placeholder="Furnished" value={furnished} onChange={e => setFurnished(e.target.value)}>
                {data.furnished.map(furnished => {
                    return (
                        <option label={furnished} value={furnished} key={furnished} />
                    )
                })}
            </Input>
            <Input type="select" placeholder="Status" value={status} onChange={e => setStatus(e.target.value)}>
                {data.status.map(status => {
                    return (
                        <option label={status} value={status} key={status} />
                    )
                })}
            </Input>
            <Input type="select" placeholder="Transaction" value={transaction} onChange={e => setTransaction(e.target.value)}>
                {data.transactions.map(transaction => {
                    return (
                        <option label={transaction} value={transaction} key={transaction} />
                    )
                })}
            </Input>
            <Input type="select" placeholder="Types" value={types} onChange={e => setType(e.target.value)}>
                {data.types.map(types => {
                    return (
                        <option label={types} value={types} key={types} />
                    )
                })}
            </Input>
            <input type={"checkbox"} checked={parking} onChange={e => setParking(e.target.checked)} /> Parking
            <Button color={'primary'} 
                onClick={() => {
                    console.log(parking)
                    Axios.post('http://localhost:5000/predict/delhi', {
                        bhk,
                        locality,
                        area,
                        bath,
                        furnished,
                        parking: parking ? 1 : 0,
                        status,
                        transaction,
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

export default Mumbai;
