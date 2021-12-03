const argv = require("./config/yargs")
const colors = require("./config/colors")


/* Obtener argumentos recibidos por el CLI
const [,,arg3='base'] = process.argv
console.log(arg3)*/

/*
Yargs permite acceder a los argumentos de una manera más elegante a través de sintáxis de JavaScript.
Muy útil para aplicaciones CLI.
*/
console.log(colors.setInfo(argv))
console.log(colors.setSuccess(argv.base))