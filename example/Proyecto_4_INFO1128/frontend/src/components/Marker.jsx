import React from "react"

import {Marker as Marcador, Popup} from "react-leaflet"
import "leaflet/dist/leaflet.css"
import { useDispatch } from "react-redux"
import { updateMaterialParticulado } from "../features/MaterialParticulado/materialSlice"

import { useMaterial } from "../custom_hooks/Material"


export const Marker = ({position, id}) => {

    // Hook de Redux para actualizar un estado almacenado en el store
    const dispatch = useDispatch()

    /*
    Custom hook que realiza una petición a la ruta set data del backend y
    obtener 30 elementos para cada material particulado con respecto al id
    asociado al marcador de una estación ambiental.
    */
    const mat = useMaterial(id,30)

    /*
    Returnar el marcador en la ubicación de la estación ambiental dada por el backend,
    React Leaflet ofrece una propiedad eventHandlers para que mediante un JSON se definan
    todos los eventos como una propiedad y su respectiva funcionalidad, para este caso,
    actualizar el estado del material particulado definido en el store.
    */
    return <Marcador position={position} eventHandlers={{
        click: () => {
            dispatch(updateMaterialParticulado(mat))
        }
    }}>
        <Popup>
            <h2 style={{textAlign: 'center'}}>Estación Ambiental: {id}</h2>
            <span>Ubicación: {position[0]},{position[1]}</span>
            <br />
        </Popup>
    </Marcador>
}