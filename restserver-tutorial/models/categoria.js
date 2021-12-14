const {Schema, model} = require("mongoose")

const CategoriasSchema = Schema({
    nombre: {
        type: String,
        required: [true, "El nombre es obligatorio"]
    }
})

module.exports = model(CategoriasSchema)