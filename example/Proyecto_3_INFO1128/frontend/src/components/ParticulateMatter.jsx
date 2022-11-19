import React from "react"
import './styles/ParticulateMatter.css'

import { Line } from 'react-chartjs-2';

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';

import { useParticulateMatter } from '../custom_hooks/Particulate_Matter'

import {Button} from "./Button"

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

const option_m = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Material Particulado',
      },
    },
}

const option_t = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Temperatura',
      },
    },
}

export const ParticulateMatter = () => {

    const {matter01, matter25, matter10, temperature, labels} = useParticulateMatter()

    const saveCanvas = (id) => {
        const cv = document.getElementById(id)
        cv.toBlob((blob) => {
            //console.log(blob)
            var data = new FormData()
            data.append('file', blob, 'file.png')

            fetch("http://localhost:8000/send-image", {
                method: "POST",
                body: data
            })
            .then(res => console.log(res.json()))
        })
    }

    const data_material = {
        labels,
        datasets: [
          {
            label: 'Material Particulado 1',
            data: matter01,
            borderColor: 'rgb(33, 158, 188)',
            backgroundColor: 'rgba(33, 158, 188, 0.5)',
          },
          {
            label: 'Material Particulado 2.5',
            data: matter25,
            borderColor: 'rgb(255, 183, 3)',
            backgroundColor: 'rgba(255, 183, 3, 0.5)',
          },
          {
            label: 'Material Particulado 10',
            data: matter10,
            borderColor: 'rgb(239, 25, 60)',
            backgroundColor: 'rgba(239, 35, 60, 0.5)',
          },
        ],
    }

    const data_temperatura = {
        labels,
        datasets: [
          {
            label: 'Temperatura',
            data: temperature,
            borderColor: 'rgb(33, 158, 188)',
            backgroundColor: 'rgba(33, 158, 188, 0.5)',
          }
        ],
    }

    return <div className="container">
        <div className="graf">
            <Line id="material_particulado" options={option_m} data={data_material} />
            <Button onClick={(e) => {saveCanvas("material_particulado")}} btn="primary" value="Botón 1" />
        </div>
        <div className="graf">
            <Line id="temperatura" options={option_t} data={data_temperatura} />
            <Button onClick={(e) => {saveCanvas("temperatura")}} btn="danger" value="Botón 2" />
        </div>
    </div>
}