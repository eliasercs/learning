import { createSlice } from "@reduxjs/toolkit";

export const materialSlice = createSlice({
    name: 'MaterialParticulado',
    initialState: {
        '01': [],
        '10': [],
        '25': [],
        'labels': [],
        'station_id': ""
    },
    reducers: {
        updateMaterialParticulado: (state, action) => {
            //console.log(action.payload)
            action.payload

            return action.payload
        }
    }
})

export const {updateMaterialParticulado} = materialSlice.actions

export default materialSlice.reducer