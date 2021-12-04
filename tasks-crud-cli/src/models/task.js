const {v4: uuidv4} = require("uuid") // Generate a unique identifier

// Class used to create tasks
class Task {
    id = ""
    description = ""
    completeIn = null

    constructor(description) {
        this.description = description
        this.id = uuidv4()
        this.completeIn = null
    }
}

module.exports = Task