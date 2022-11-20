import React from "react"

import {Polyline} from "react-leaflet"


export const DrawLine = ({options, color, route}) => {

    return <Polyline pathOptions={options[color]} positions={route} />

}