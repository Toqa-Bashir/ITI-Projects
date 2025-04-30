const express = require("express");
const userController = require ("../Controllers/userController"); 
const auth = require("../middleware/auth")
const restrictTo = require("../middleware/restrictTo");

const router = express.Router()

//POST users 
router.post("/signIn",userController.signIn);
router.post("/login",userController.login);

//GET all users
router.get("/",auth , restrictTo("admin"),userController.getallUsers)

//GET user by id 
router.get("/:id",userController.getOneUser)

//UPDATE user by id 
router.patch("/:id",userController.updateOneUser)

//DELETE user by id 
router.delete("/:id",userController.deleteOneUser)

module.exports = router;
