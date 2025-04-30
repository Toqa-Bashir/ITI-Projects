

const Post = require("../Models/Postmodel");

const createPost = async(req , res)=>{
    const { title , content } = req.body;
    const post =  await Post.create({ title , content });
    res.status(201).json({
      message: "Post created successfully",
      data: {
        post,
      },
    });
  };

  const getallPosts = async(req , res)=>{
    const posts =await Post.find()
    res.status(200).json({
      message:"Post fetched succesfully ",
      data :{ posts}
    });
  }


  const getOnePost = async(req , res)=>{
    const {id} = req.params;
    const post = await Post.findOne({_id:id});
    res.status(200).json({
      message:"Post fetched succesfully ",
      data :{ post}
    });
  }

  const updateOnePost = async(req,res)=>{
    const {id} = req.params;
    const post = await Post.findByIdAndUpdate({_id : id});
    res.status(200).json({
      message:"Post updated succesfully ",
      data :{ post}
    });
  }

  const deleteOnePost = async(req , res)=>{
    const {id} = req.params;
    const post = await Post.findOneAndDelete({_id : id});
    res.status(200).json({
      message:"Post deleted succesfully ",
      data :{ post}
    }); 
  }

  module.exports = {
    createPost , getallPosts , getOnePost , updateOnePost , deleteOnePost
  }

//   console.log(__dirname);
// console.log(require.resolve("./../Models/postModel"));