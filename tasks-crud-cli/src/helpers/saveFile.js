const fs = require("fs")

const file = "./src/db/data.json"

// Save the information in data.json
const saveDB = (data) => {
    fs.writeFileSync(file,JSON.stringify(data))
}

// Get the information of data.json
const readDB = () => {
    if (!fs.existsSync(file)){
        return null
    }
    const info = fs.readFileSync(file,{
        encoding: "utf-8"
    })

    const data = JSON.parse(info)
    return data
}

// Export each function
module.exports = {
    saveDB,
    readDB
}