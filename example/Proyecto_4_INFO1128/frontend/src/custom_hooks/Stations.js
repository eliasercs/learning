import { useState, useEffect } from "react";

export const useStations = () => {

    const [stations, setStations] = useState([])

    useEffect(() => {
        const url = "http://127.0.0.1:8000/get-stations"
        const request = async () => {
            const response = await fetch(url)
            const data = await response.json()
            setStations(data)
        }

        request()
        .catch(err => console.log(err))
    }, [])

    return {
        stations
    }
}