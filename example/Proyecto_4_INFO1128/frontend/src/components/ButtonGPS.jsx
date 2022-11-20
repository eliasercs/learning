import React from "react";
import { useDispatch } from "react-redux";
import { useVehicle } from "../custom_hooks/Vehicle";
import { updateRouteGPS } from "../features/routeGPS/routeSlice";
import { updateColorGPS } from "../features/routeGPS/colorSlice";

export const ButtonGPS = ({id}) => {

    /*
    Definir una lista de con estilos personalizados para cada Polyline renderizado en el mapa
    */
    const colors = [
        { color: "#fca311" },
        { color: "#ef233c" },
        { color: "#06d6a0" },
        { color: "#7209b7" },
        { color: "#f72585" },
        { color: "#003049" },
        { color: "#5f0f40" },
        { color: "#e36414" },
        { color: "#0081a7" },
        { color: "#252422" }
    ]

    const dispatch = useDispatch()
    // Obtener la ruta del vehículo seleccionado
    const route = useVehicle(id)

    // Mediante un evento click actualizar el estado del color de la ruta y la ruta misma.
    const handleClick = (e) => {
        dispatch(updateRouteGPS(route))
        dispatch(updateColorGPS(colors[id]))
    }

    return <button id={id} onClick={handleClick} style={{padding: "20px"}}>Vehiculo {id}</button>
}