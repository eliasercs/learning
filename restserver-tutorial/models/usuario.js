const {Schema, model} = require("mongoose")

const UsuarioSchema = Schema({
    nombre: {
        type: String, // Tipo de dato
        required: [true, "El nombre es obligatorio"] // Registro obligatorio
    },
    correo: {
        type: String,
        required: [true, "El correo es obligatorio"],
        unique: true // Registro único
    },
    password: {
        type: String,
        required: [true, "La contraseña es obligatoria"]
    },
    image: {
        type: String
    },
    rol: {
        type: String,
        required: true,
        enum: ["ADMIN_ROLE","USER_ROLE"] // Validar el rol del usuario
    },
    estado: {
        type: Boolean,
        default: true // Valor por defecto
    },
    google: {
        type: Boolean,
        default: false
    }
})

module.exports = model("Usuario", UsuarioSchema)