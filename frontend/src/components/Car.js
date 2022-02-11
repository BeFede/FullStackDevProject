const App = ({car}) => {    
    return (        
        <div>
            <p><span style={{ fontWeight: 'bold' }}>Plate:</span> {car.plate}</p>
            <p><span style={{ fontWeight: 'bold' }}>Name:</span> {car.name}</p>
        </div>
    )
}

export default App;