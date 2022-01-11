import React, {useEffect, useRef} from "react"
import * as THREE from "three"
import {OrbitControls} from "three/examples/jsm/controls/OrbitControls"
//import blue from "./static/textures/blue.jpg"
import textura from "./static/textures/1051.jpg"

function App() {

  const mountRef = useRef(null) // Referencia al elemento en el DOM

  useEffect(()=>{

    const texture = new THREE.TextureLoader().load(textura)
    texture.wrapS = THREE.RepeatWrapping
    texture.wrapT = THREE.RepeatWrapping
    //texture.repeat.set(4,4)


    const currentRef = mountRef.current //Referencia actual del elemento
    const {clientWidth:width, clientHeight:height} = currentRef

    const Scene = new THREE.Scene()
    const Camera = new THREE.PerspectiveCamera(25, width/height, 0.5, 1000)
    Camera.position.z = 10
    Camera.position.y = 10

    Scene.add(Camera)
    
    const Geometry = new THREE.BoxGeometry(4,2,2)
    const Material = new THREE.MeshBasicMaterial({map: texture})

    const Cube = new THREE.Mesh(Geometry,Material)

    Camera.lookAt(Cube.position)
    Scene.add(Cube)

    const Renderer = new THREE.WebGLRenderer()
    Renderer.setSize(width,height)

    currentRef.appendChild(Renderer.domElement)
    
    const controls = new OrbitControls(Camera,Renderer.domElement)
    controls.enableDamping = true
    const animate = () => {
      controls.update()
      requestAnimationFrame(animate)
      Cube.rotation.x += 0.02
      Cube.rotation.y += 0.02
      Renderer.render(Scene,Camera)
    }

    animate()
    //Renderer.render(Scene,Camera)

    return () => {
      currentRef.removeChild(Renderer.domElement)
    }
  },[])

  return (
    <div ref={mountRef} className="App" style={{width:"100%", height: "100vh"}}>

    </div>
  );
}

export default App;
