const {Router} = require("express")
const { getUsers, saveUser } = require("../controllers/users.controller")
const router = Router()

router.get("/",getUsers)
router.post("/:id",saveUser)

module.exports = router