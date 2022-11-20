import { createSlice } from "@reduxjs/toolkit"

export const routeSlice = createSlice({
    name: 'Route',
    initialState: [],
    reducers: {
        updateRouteGPS: (state, action) => {
            //console.log(action.payload)
            state = action.payload

            return action.payload
        }
    }
})

export const {updateRouteGPS} = routeSlice.actions

export default routeSlice.reducer
