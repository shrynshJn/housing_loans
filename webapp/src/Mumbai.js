import React, { useState, useEffect } from 'react';
import { Input, Button } from "reactstrap";
import Axios from 'axios';

const Mumbai = (props) => {
    const [data, setData] = useState({locality: [], furnished: [], types: []});
    const [locality, setLocality] = useState("");
    const [bed, setBed] = useState("");
    const [area, setArea] = useState("");
    const [furnished, setFurnished] = useState("");
    const [types, setType] = useState("");
    const [bath, setBath] = useState("");
    const [floor_count, setFloorCount] = useState("");
    const [floor_num, setFloorNumber] = useState("");    
    
    useEffect(() => {
        Axios.get('http://localhost:5000/data/mumbai')
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
            <Input type="number" placeholder="Beds" min={1} step={1} value={bed} onChange={e => setBed(e.target.value)} />
            <Input type="number" placeholder="Area" min={0} step={100} value={area} onChange={e => setArea(e.target.value)} />
            <Input type="select" placeholder="Furnished" value={furnished} onChange={e => setFurnished(e.target.value)}>
                {data.furnished.map(furnished => {
                    return (
                        <option label={furnished} value={furnished} key={furnished} />
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
            <Input type="number" placeholder="Baths" min={0} step={1} value={bath} onChange={e => setBath(e.target.value)} />
            <Input type="number" placeholder="Floor Count" min={0} step={1} value={floor_count} onChange={e => setFloorCount(e.target.value)} />
            <Input type="number" placeholder="Floor Number" min={0} step={1} value={floor_num} onChange={e => setFloorNumber(e.target.value)} />
            <Button color={'primary'} 
                onClick={() => {
                    Axios.post('http://localhost:5000/predict/mumbai', {
                        locality,
                        bed,
                        area,
                        furnished,
                        types,
                        bath,
                        floor_count,
                        floor_num
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
