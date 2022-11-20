import { useState, useEffect } from "react";

export const useMaterial = (id,number) => {

    const [material, setMaterial] = useState([])

    useEffect(() => {

        const url = `http://localhost:8000/set-data/${id}/${number}`
        const request = async () => {
            const response = await fetch(url)
            const data = await response.json()
            return data
        }

        request()
        .then(data => {
            if (data["msg"] === "Error") {
                console.log("Error")
            } else {
                setMaterial(data)
            }
            
        })
        .catch(err => console.log(err))
    },[])

    return material
}