const colors = require("colors")

colors.setTheme({
    error: "red",
    success: "green",
    warning: "yellow",
    info: "blue",
    help: "gray"
})

const setError = (e) => colors.error(e)
const setInfo = (e) => colors.info(e)
const setSuccess = (e) => colors.success(e)
const setWarning = (e) => colors.warning(e)
const setHelp = (e) => colors.help(e)

module.exports = colors
module.exports.setError = setError
module.exports.setInfo = setInfo
module.exports.setSuccess = setSuccess
module.exports.setWarning = setWarning
module.exports.setHelp = setHelp