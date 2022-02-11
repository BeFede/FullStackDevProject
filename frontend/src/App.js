import './App.css';
import { useState } from 'react';
import './header.css'
import './container.css'
import ContentAppPage from './components/ContentAppPage'
import FormCarPlate from './components/FormCarPlate'
import CarService from './services/carService'

const App = () => {
        
    // Define data and hooks to use
    const [valuesForm, setValue] = useState({ plate: ""})
    const [errorMessage, setErrorMessage] = useState("")
    const [car, setCar] = useState({ id: "", plate: "", name: ""})

    const submit = e => {
        e.preventDefault()
        
        // Callback function to execute if the request is success
        const callback = (car) => {
            setErrorMessage("")
            setCar({
                id: car.id,
                name: car.name,
                plate: car.plate,
            })

            // Clean input
            setValue({...valuesForm, plate: ""})
        }
        CarService.getByPlate(valuesForm.plate, callback, setErrorMessage)                       
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
                <FormCarPlate onSubmit={submit} plate={valuesForm.plate} handleChange={handleChange} />                                
            </header>
            <div className="container" >    
                <ContentAppPage car={car} errorMessage={errorMessage} ></ContentAppPage>
                                                                                               
            </div>            
        </div>
    );
}

export default App;