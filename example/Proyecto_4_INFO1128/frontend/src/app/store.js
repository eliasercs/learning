import { configureStore } from '@reduxjs/toolkit'

import materialReducer from '../features/MaterialParticulado/materialSlice'
import routeReducer from '../features/routeGPS/routeSlice'
import colorReducer from '../features/routeGPS/colorSlice'

export const store = configureStore({
    reducer: {
        material: materialReducer,
        route: routeReducer,
        color: colorReducer
    }
})