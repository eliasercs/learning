import React, { useEffect } from "react";
import { useState } from "react";

export const useParticulateMatter = () => {

    const [matter01,setMatter01] = useState([])
    const [matter25,setMatter25] = useState([])
    const [matter10,setMatter10] = useState([])
    const [temperature,setTemperature] = useState([])
    const [labels, setLabels] = useState([])

    useEffect(() => {

        const url = 'http://localhost:8000/get-data'

        const fetchData = async () => {
            const response = await fetch(url)
            const json = await response.json()
            setMatter01(json['01'])
            setMatter25(json['25'])
            setMatter10(json['10'])
            setTemperature(json['te'])
            setLabels(json['labels'])
        }

        fetchData()

    }, [])

    return {
        matter01,
        matter25,
        matter10,
        temperature,
        labels
    }

}