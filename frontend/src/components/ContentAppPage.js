import Car from './Car'
import CustomMessage from './CustomMessage'

const ContentAppPage = ({car, errorMessage}) => {

    return (
        errorMessage === "" 
        ? ( 
            car.plate !== "" ? 
                <Car car={car} />  
                : 
                <CustomMessage type="normal">
                    Please type the car plate
                </CustomMessage>
            )
        : 
        <CustomMessage type="error">{errorMessage}</CustomMessage>     
    )
}

export default ContentAppPage;