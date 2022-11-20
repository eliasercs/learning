import React from "react"
import { Stations } from "./pages/Stations"
import { GPS } from "./pages/GPS"
import {Route, useLocation} from 'wouter'
import "./assets/css/index.css"

function App() {

  const [location, setLocation] = useLocation()

  return (
    <div className="App">
      <Route path="/">
        <button onClick={() => setLocation("/stations")}>Estaciones Ambientales</button>
        <button onClick={() => setLocation("/gps")}>Rutas GPS</button>
      </Route>
      <Route path="/stations"><Stations /></Route>
      <Route path="/gps"><GPS /></Route>
    </div>
  )
}

export default App
