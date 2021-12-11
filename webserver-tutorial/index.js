const express = require("express")
const app = express()
const hbs = require("hbs")

app.set('view engine', 'hbs') // La idea de handlebar es utilizar el patrón MVC
hbs.registerPartials(__dirname + '/views/partials', function (err) {});
// Servir contenido estático
app.use(express.static('public')) // express.static tiene mayor prioridad que las rutas definidas

app.get("/",(req,res) => {
    res.render("home",{
        titulo: "Hola Mundo"
    })
})

app.get("/elements", (req,res) => {
    res.render("elements")
})

app.get("/generic", (req,res) => {
    res.render("generic")
})

app.get("*", (req,res) => {
    res.sendFile(__dirname+"/public/error404.html")
})

app.listen(8080)