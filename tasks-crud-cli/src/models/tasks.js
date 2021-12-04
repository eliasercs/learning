const Task = require("./task")
const colors = require("../config/colors")

//Class used to apply CRUD operations in the tasks
class Tasks {
    _list = {}
    // Get the tasks as a list
    get getList() {
        let list = []
        Object.keys(this._list).forEach(key=>list.push(this._list[key]))
        return list
    }
    // Initialize the class
    constructor() {
        this._list = {}
    }
    // Transform a to-do list into a JavaScript Object
    loadTasksFromArray(tasks = []) {
        tasks.forEach(item => {
            this._list[item.id] = item
        })
    }
    // Create a task
    createTask(description="") {
        let task = new Task(description)
        this._list[task.id] = task
    }
    // Show all tasks
    listTasks() {
        this.getList.map((item,index) => {
            console.log(`${colors.setSuccess(index+1)}. ${item.description} :: ${item.completeIn===null ? colors.setWarning('Pending') : colors.setSuccess('Completed')}`)
        })
    }
    // Show all pending or completed tasks
    listPendingOrCompletedTasks(completed = true) {
        let count = 0
        this.getList.map((item) => {
            const {description, completeIn} = item
            if (completed) {
                count += 1
                if (completeIn) {
                    console.log(`${colors.setSuccess(count)}. ${colors.setInfo(description)} :: completed in: ${colors.setSuccess(completeIn)}`)
                }
            } else {
                count += 1
                if (!completeIn) {
                    console.log(`${colors.setWarning(count)}. ${colors.setError(description)}`)
                }
            }
        })
    }
    // Delete a task
    deleteTask(id='') {
        if (this._list[id]) {
            delete this._list[id]
            return true
        }
        return false
    }

    // Complete one o more tasks
    completeTasks(ids = []){
        // Mark a task as completed including the date
        ids.forEach(id => {
            const task = this._list[id]
            if (!task.completeIn) {
                task.completeIn = new Date().toISOString()
            }
        })
        // Mark a task as pending and remove the date
        this.getList.forEach(task => {
            if (!ids.includes(task.id)){
                this._list[task.id].completeIn = null
            }
        })
    }
}

module.exports = Tasks