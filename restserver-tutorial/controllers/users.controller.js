const {response,request} = require("express")

const getUsers = (req=request,res=response) => {
    const {name=null, lastname=null} = req.query // Parámetros de consultas (son opcionales)
    res.json({
        msg: "Get a user",
        name,
        lastname
    })
}

const saveUser = (req=request,res=response) => {
    const body = req.body // Enviar información mediante el body
    const {id} = req.params
    res.json({
        msg: "Post - Save a user",
        id,
        body
    })
}

module.exports = {
    getUsers,
    saveUser
}