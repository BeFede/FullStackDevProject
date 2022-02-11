import Config from '../helpers/config'

const CarService = {

    getByPlate: (plate, callbackSuccess, callbackError) => {
        if (plate === "") {
            callbackError("The plate parameter is required")
            return
        }

        // create file services
        // http requet to get car data from the specified plate 
        fetch(`${Config.url}cars/${plate}`).then(async res => {            
            if (res.status === 200){
                const data = await res.json()
                callbackSuccess(data.content.car)
            } 
            else if (res.status === 404){
                callbackError("The car plate " + plate.toString() + " was not found")
            } 
            else {                
                callbackError("A server error has ocurred. Please contact administrator")
            }
        }).catch(err => {
            callbackError("A server error has ocurred. Please contact administrator")
        }) 

    }
}

export default CarService