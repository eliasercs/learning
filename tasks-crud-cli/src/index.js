const { inquirerMenu, pause, readInput, deleteTaskOfList, confirm, inquirerTasks } = require("./helpers/inquirer");
const { saveDB, readDB } = require("./helpers/saveFile");
const Tasks = require("./models/tasks")
const colors = require("./config/colors")

console.clear()
const main = async () => {

    let opt = ""
    const tasks = new Tasks()
    let tasksDB = readDB() // Get data of the file "data.json"
    if (tasksDB) {
        tasks.loadTasksFromArray(tasksDB) // Load the tasks of data.json if data exist
    }

    do {
        opt = await inquirerMenu() //Show menu

        switch (opt) { //Evaluate options
            case "1": // Create a task
                const desc = await readInput("Description: ") //Request a description
                tasks.createTask(desc)
                break
            case "2": // List all tasks
                tasks.listTasks()
                break
            case "3": // List completed tasks
                tasks.listPendingOrCompletedTasks()
                break
            case "4": // List pendings tasks
                tasks.listPendingOrCompletedTasks(false)
                break
            case "5": // Complete a task
                let ids = await inquirerTasks(tasks.getList)
                tasks.completeTasks(ids)
            break
            case "6": // Delete a task
                const id = await deleteTaskOfList(tasks.getList)
                if (id!=='0') {
                    let ok = confirm("Are you sure to delete this task?")
                    await pause()
                    if (ok) {
                        let deleted = tasks.deleteTask(id)
                        console.log(deleted ? colors.setSuccess("Task removed successfully") : colors.setError("Failed to delete task"))
                    }
                }
                break
        }

        saveDB(tasks.getList) // Save the data in the file "data.json"

        await pause()
    } while (opt!=="7");

}

main()