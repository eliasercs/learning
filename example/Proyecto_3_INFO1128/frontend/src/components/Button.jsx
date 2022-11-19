import React from "react";
import PropTypes from "prop-types"

export const Button = ({value, btn, onClick}) => {
    return <button 
        className={"btn "+btn}
        onClick={onClick}
    >{ value }</button>
}

Button.propTypes = {
    value: PropTypes.string.isRequired,
    btn: PropTypes.string.isRequired,
    onClick: PropTypes.func
}