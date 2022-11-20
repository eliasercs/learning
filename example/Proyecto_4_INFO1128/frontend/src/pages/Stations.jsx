import React from "react"
import { Chart } from "../components/Chart"

import { MapContainer, TileLayer, ZoomControl } from 'react-leaflet'
import "leaflet/dist/leaflet.css"

import { Marker } from "../components/Marker"
import { useStations } from "../custom_hooks/Stations"

import { useSelector } from "react-redux"

export const Stations = () => {

    // Obtener de forma dinámica cada una de las estaciones
    const { stations } = useStations()

    // Obtener el estado actual del material particulado.
    const materialState = useSelector(state => state.material)
    console.log(materialState)

    /*
    Para cada material particulado, se desarrolla un JSON con propiedades como su label,
    su información, el color de fondo y borde de la línea.
    */
    const datos = [
        {
            label: 'Material Particulado 1',
            data: materialState['01'],
            borderColor: 'rgb(144, 190, 109)',
            backgroundColor: 'rgba(144, 190, 109, 0.5)',
        },
        {
            label: 'Material Particulado 2.5',
            data: materialState['25'],
            borderColor: 'rgb(248, 150, 30)',
            backgroundColor: 'rgba(248, 150, 30, 0.5)',
        },
        {
            label: 'Material Particulado 10',
            data: materialState['10'],
            borderColor: 'rgb(249, 65, 68)',
            backgroundColor: 'rgba(249, 65, 68, 0.5)',
        }
    ]

    return <div className="stations-container">

        <MapContainer center={[-38.7379, -72.6005]} zoom={14.5} scrollWheelZoom={false} style={{height: '400px'}}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {
                /*
                Dentro del mapa, se obtiene de forma dinámica cada una de las estaciones y para cada una se renderiza
                su respectivo marcador en la posición dada.
                */
                stations.map((element, key) => (<Marker 
                    position={[element['x'], element['y']]} 
                    key={key} 
                    id={element['id']} 
                />))
            }
        </MapContainer>
        
        {
            /*
            Si al obtener el estado del material particulado, existe información cargada.
            Sólo en ese casom se renderiza el comoponente del gráfico con las propiedades solicitadas
            para el componente.
            */
            materialState['station_id'] !== '' && <Chart data={datos} labels={materialState['labels']} station_id={materialState['station_id']} />
        }

    </div>
}