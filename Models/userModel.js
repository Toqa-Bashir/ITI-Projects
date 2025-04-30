const { default: mongoose } = require("mongoose");

const userSchema = new mongoose.Schema({
    name: {type : String, required: true} , 
    age: {type : Number },
    email:{type : String , required : true ,match: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,} , 
    password:{type:String , required : true},
    confirm_pass : {type : String , required : true},
    role:{ type : String , required:true , enum:["user" , "admin"], default:"user"}
  });

const User = mongoose.model("User",userSchema);
 module.exports=User 