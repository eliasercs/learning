import { useState, useEffect } from "react";

export const useAllVehicles = () => {

    const [vehicles, setVehicles] = useState([])

    useEffect(() => {
        const url = `http://localhost:8000/get-vehicles`

        const request = async () => {
            const response = await fetch(url)
            const data = await response.json()
            return data
        }

        request()
        .then(data => {
            setVehicles(data.id)
        })
    }, [])

    return vehicles
}