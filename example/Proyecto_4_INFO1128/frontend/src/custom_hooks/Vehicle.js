import { useState, useEffect } from "react";

export const useVehicle = (id) => {

    const [route, setRoute] = useState([])

    useEffect(() => {
        const url = `http://localhost:8000/get-gps/${id}`

        const request = async () => {
            const response = await fetch(url)
            const data = await response.json()
            return data
        }

        request()
        .then(data => {
            var values = []
            data.forEach((value) => {
                values.push([value.lat, value.lon])
            })
            setRoute(values)
        })
    }, [])

    return route
}