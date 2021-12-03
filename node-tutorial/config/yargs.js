let colors = require("./colors")

const argv = require('yargs')
            .option(colors.setSuccess('b'),{  // Se utiliza option para definir o crear argumentos
                alias: colors.setSuccess('base'), // Nombre de argumento
                type: "number", // Tipo de dato al que representa
                demandOption: true, //Requiere un valor obligatorio
                describe: colors.setInfo("Es un número base") //Descripción del argumento
            })
            .option(colors.setSuccess('l'),{
                alias: colors.setSuccess('listar'),
                type: "boolean",
                default: false,
                describe: colors.setInfo("Muestra una lista de algo")
            })
            .check( (argv, options) => { //Verifica que ciertas condiciones se cumplan al recibir el argumento
                if (isNaN(argv.b)) {
                    throw(colors.setWarning("Argumento base tiene que ser un número"))
                }
                return true
            } )
            .argv

module.exports = argv