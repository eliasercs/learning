const express = require("express")
const cors = require("cors")

class Server {
    constructor() {
        this.app = express()
        this.port = process.env.PORT 

        this.middlewares()
        this.routes()
    }

    middlewares() {
        this.app.use(cors()) // Cors
        this.app.use(express.json()) //Lectura y parseo del body
    }

    routes() {
        this.app.use("/api/users",require("../routes/users.route"))
    }

    listen(){
        this.app.listen(this.port, () => console.log("Aplication listening in the port",this.port))
    }

}

module.exports = {
    Server
}