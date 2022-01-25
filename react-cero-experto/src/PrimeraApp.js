import React from 'react';
import PropTypes from "prop-types";

const PrimeraApp = ({name}) => {
  // Los props o properties son propiedades de un JSON.
  //console.log(props)

  return <div>
      <h1>Hola {name}</h1>
  </div>;
};

PrimeraApp.propTypes = { // Define los tipos de propiedades que debe recibir nuestro componente
    name: PropTypes.string.isRequired // Propiedad de tipo string obligatoria
}

PrimeraApp.defaultProps = { // Define los valores por defecto de las propiedades
    name: "Mundo"
}

export default PrimeraApp;
