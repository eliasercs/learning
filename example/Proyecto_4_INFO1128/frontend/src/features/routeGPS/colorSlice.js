import { createSlice } from "@reduxjs/toolkit"

export const colorSlice = createSlice({
    name: 'Color',
    initialState: "",
    reducers: {
        updateColorGPS: (state, action) => {
            //console.log(action.payload)
            state = action.payload

            return action.payload
        }
    }
})

export const {updateColorGPS} = colorSlice.actions

export default colorSlice.reducer