import React from "react"

import { MapContainer, TileLayer, Polyline } from 'react-leaflet'
import "leaflet/dist/leaflet.css"
import { useAllVehicles } from "../custom_hooks/AllVehicles"
import { useSelector } from "react-redux"
import { ButtonGPS } from "../components/ButtonGPS"

export const GPS = () => {

    // Custom Hook que realiza una petición al backend y obtiene todos los vehículos
    const vehicles = useAllVehicles()
    // Obtener el estado global para la ruta del vehículo
    const route = useSelector(state => state.route)
    // Obtener el estado global para el color de la ruta
    const color = useSelector(state => state.color)

    return <div>
        <MapContainer center={[-38.7379, -72.6005]} zoom={14.5} scrollWheelZoom={false} style={{height: '100vh'}}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Polyline pathOptions={color} positions={route} />            
        </MapContainer>
        {
            /*
            Obtener los vehículos y de manera dinámica renderizar un botón para cada uno de ellos.
            */
            vehicles.map((value, key) => {
                return <ButtonGPS key={key} id={value} />
            })
        }
    </div>
}