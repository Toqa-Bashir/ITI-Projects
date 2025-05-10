const { default: mongoose } = require("mongoose");

const postSchema = new mongoose.Schema({
    title: {type : String, required: true, enum:["Student","Teacher","Supervisor","Worker"], default:"Worker"},
    content:{type: String,required : true , minlength : 20 , maxlength : 100 }
  });

const Post = mongoose.model("Post",postSchema);
 module.exports=Post