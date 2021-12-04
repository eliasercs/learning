const colors = require("../config/colors")

const showMenu = () => {

    return new Promise(resolve=>{
        console.clear()
        console.log(colors.setSuccess("==================================="))
        console.log(colors.setSuccess("       Seleccione una opción       "))
        console.log(colors.setSuccess(`===================================\n`))
    
        console.log(`${colors.setSuccess("1.")} Create a task`)
        console.log(`${colors.setSuccess("2.")} Read assignments`)
        console.log(`${colors.setSuccess("3.")} Read completed tasks`)
        console.log(`${colors.setSuccess("4.")} Read pending tasks`)
        console.log(`${colors.setSuccess("5.")} Complete tasks`)
        console.log(`${colors.setSuccess("6.")} Delete a task`)
        console.log(`${colors.setSuccess("7.")} Exit \n`)
    
        const readline = require("readline").createInterface({
            input: process.stdin,
            output: process.stdout
        })
    
        readline.question(colors.setInfo("Select a option: "), (opt) => {
            readline.close()
            resolve(opt)
        })
    })

}

const pause = () => {

    return new Promise(resolve => {
        const readline = require("readline").createInterface({
            input: process.stdin,
            output: process.stdout
        })
    
        readline.question(colors.setInfo(`PRESS THE ${colors.setWarning("ENTER KEY")} to continue \n`), (opt) => {
            readline.close()
            resolve()
        })
    })

}

module.exports = {
    showMenu,
    pause
}