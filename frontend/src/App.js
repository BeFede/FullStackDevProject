import './App.css';
import { useState } from 'react';
import Car from './components/Car'
import './header.css'
import './container.css'
import CustomMessage from './components/CustomMessage'

const App = () => {

    const url = "http://localhost:8000/api/"

    // Another option is use Formik that simplified this code
    const [valuesForm, setValue] = useState({ plate: ""})
    const [errorMessage, setErrorMessage] = useState("")
    const [car, setCar] = useState({ id: "", plate: "", name: ""})

    const submit = e => {
        e.preventDefault()
        
        if (valuesForm.plate == "") {
            setErrorMessage("The plate is required")
            return
        }

        // http requet to get car data from the specified plate 
        fetch(`${url}cars/${valuesForm.plate}`).then(async res => {            
            if (res.status == 200){
                const data = await res.json()
                setErrorMessage("")
                setCar({
                    id: data.content.car.id,
                    name: data.content.car.name,
                    plate: data.content.car.plate,
                })
                setValue({...valuesForm, plate: ""})
            } 
            else if (res.status === 404){
                setErrorMessage("The car with plate " + valuesForm.plate.toString() + " was not found")
            } 
        }).catch(err => {
            setErrorMessage("Fatal error ")
        })                
    }

    const handleChange = (e) => {
        e.preventDefault()
        setValue({
            ...valuesForm,
            [e.target.name]: e.target.value
        })

    }

    return ( 
        <div>
            <header>
                <form onSubmit = { submit } >
                    <input type="text" name="plate" value={valuesForm.plate} onChange={handleChange} />
                    <input type="submit" value="Search" />
                </form>
                
            </header>
            <div className="container" >                                               
                { errorMessage == "" 
                    ? ( 
                        car.plate != "" ? 
                            <Car car={car} />  
                            : 
                            <CustomMessage type="normal">
                                Insert the plate to get the car
                            </CustomMessage>
                        )
                    : 
                    <CustomMessage type="error">{errorMessage}</CustomMessage> 
                }                                                                               
            </div>            
        </div>
    );
}

export default App;