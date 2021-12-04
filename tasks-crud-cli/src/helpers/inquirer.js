const inquirer = require("inquirer")
const colors = require("../config/colors")

const menuOptions = [
    {
        type: "list",
        name: "option",
        message: "Select a option",
        choices: [{
            value: "1",
            name: `${colors.setSuccess("1.")} Create a task`
        },
        {
            value: "2",
            name: `${colors.setSuccess("2.")} Read assignments`
        },
        {
            value: "3",
            name: `${colors.setSuccess("3.")} Read completed tasks`
        },
        {
            value: "4",
            name: `${colors.setSuccess("4.")} Read pending tasks`
        },
        {
            value: "5",
            name: `${colors.setSuccess("5.")} Complete tasks`
        },
        {
            value: "6",
            name: `${colors.setSuccess("6.")} Delete a task`
        },
        {
            value: "7",
            name: `${colors.setSuccess("7.")} Exit`
        }
        ]
    }
]

// This is a initial Menu Option
const inquirerMenu = async () => {
    console.clear()
    console.log(colors.setWarning("==================================="))
    console.log(colors.setWarning("            CLI of tasks           "))
    console.log(colors.setWarning(`===================================\n`))

    const { option } = await inquirer.prompt(menuOptions)
    return option
}

// Allow pause the execution of other instruction
const pause = async () => {
    let option = [{
        type: "input",
        name: "pause",
        message: colors.setInfo(`PRESS THE ${colors.setWarning("ENTER KEY")} TO CONTINUE`),
        default: ""
    }]
    console.log("\n")
    await inquirer.prompt(option)
}

// Lets read what is entered by the user
const readInput = async (message) => {
    const question = [{
        type: "input",
        name: "description",
        message,
        validate(value) {
            if (value.length === 0) {
                return "Please enter a value"
            }
            return true
        }
    }]
    const { description } = await inquirer.prompt(question)
    return description
}

// Allow get the id of a task to delete
const deleteTaskOfList = async (tasks = []) => {

    const choices = tasks.map((task, id) => {
        const idx = colors.setSuccess(id + 1)
        return {
            value: task.id,
            name: `${idx}. ${task.description}`
        }
    })

    choices.unshift({ value: '0', name: "0. Back" })

    const queries = [{
        type: "list",
        name: "id",
        message: "Delete a task",
        choices
    }]

    const { id } = await inquirer.prompt(queries)
    return id
}

// This is a message of confirmation
const confirm = async (message) => {
    const question = [{
        type: "confirm",
        name: "ok",
        message
    }]

    const { ok } = await inquirer.prompt(question)
    return ok
}

// Return a list of "ids" of tasks
const inquirerTasks = async (tasks = []) => {
    const choices = tasks.map((task, i) => {
        const { id, description, completeIn } = task
        const idx = colors.setSuccess(i + 1)
        return {
            value: id,
            name: `${idx}. ${description}`,
            checked: completeIn ? true : false
        }

    })

    const query = [{
        type: "checkbox",
        name: "ids",
        message: "Select",
        choices
    }]

    const { ids } = await inquirer.prompt(query)
    return ids
}

// Export each function to be used later
module.exports = {
    inquirerMenu,
    pause,
    readInput,
    deleteTaskOfList,
    confirm,
    inquirerTasks
}