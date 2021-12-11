const http = require('http')

http.createServer((req,res) => {

    res.writeHead(200, {
        "Content-Type": "application/json"
    })

    const persona = {
        id: 1,
        nombre: "Eliaser"
    }

    res.write(JSON.stringify(persona))
    res.end()
})
.listen(4000)
console.log("Listening in the port", 4000)