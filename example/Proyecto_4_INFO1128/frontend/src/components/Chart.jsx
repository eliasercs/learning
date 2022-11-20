import React from 'react';
import PropTypes from 'prop-types'

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

import { Line } from 'react-chartjs-2';

// Definir los componentes de CHART JS a utilizar globalmente en todos los gráficos que se generen
ChartJS.register(
    CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend
)

/*
Mediante desestructuración, se definen las propiedades correspondientes para que este componente funcione.
@data -> lista de objetos JSON con las propiedades como tipo de gráfico y color de su respectiva información a representar
@labels -> Valores a insertar en el eje horizontal (x)
@station_id -> El número que representa a la estación ambiental
*/
export const Chart = ({data, labels, station_id}) => {

    // Configurar y/o personalizar el gráfico
    const options = {
        responsive: true, // Gráfico adaptable a distintas resoluciones de pantalla
        plugins: {
            legend: {
                position: 'top', // Posicionar la leyenda en la parte superior del gráfico
            },
            title: { // Mostrar y definir un título al gráfico
                display: true, 
                text: `Estación Ambiental: ${station_id}`,
            },
        },
        scales : { // Definir o mostrar un título a cada eje
            y: {
                title : {
                    display: true,
                    text: 'ug/m3'
                }
            },
            x: {
                title : {
                    display: true,
                    text: 't(d)'
                }
            }
        }
    }

    const datasets = { // Las propiedades de cada datasets vienen incluidas en una lista que viene en data
        labels,
        datasets: data
    }

    return <Line options={options} data={datasets} />

}

// Definit el tipo de dato de cada propiedad y solicitarlos obligatoriamente
Chart.propTypes = {
    data: PropTypes.array.isRequired,
    labels: PropTypes.array.isRequired
}