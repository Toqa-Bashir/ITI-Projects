const express = require("express");
const postController = require("./../Controllers/postController");


const router = express.Router()

//POST posts
router.post("/",postController.createPost);

//GET all posts 
router.get("/",postController.getallPosts)

//GET post by id 
router.get("/:id",postController.getOnePost)

//UPDATE post by id 
router.patch("/:id",postController.updateOnePost)

//DELETE post by id 
router.delete("/:id",postController.deleteOnePost)

module.exports = router;