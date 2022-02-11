const FormCarPlate = ({plate, handleChange, onSubmit}) => {

    return (
        <form onSubmit = { onSubmit } >
            <input type="text" name="plate" autoComplete='off' value={plate} onChange={handleChange} />
            <input type="submit" value="Search" />
        </form>  
    )
}

export default FormCarPlate;