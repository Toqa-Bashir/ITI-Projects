const User = require("../Models/userModel")
const util = require("util");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const APIError = require("./../utilis/APIErrors")


const jwtSign = util.promisify(jwt.sign);


const signIn = async(req,res,next)=>{
  try{
const { name , age , email , password , confirm_pass , role } = req.body;
if (password !== confirm_pass) {
  return res.status(400).json({ error: "Password and confirm password must match" });
  }
   const saltRounds = parseInt(process.env.SALT_ROUNDS) || 10
   const hashedpass = await bcrypt.hash(password, saltRounds);
console.log("👉👉hashedPassword", hashedpass)
 const user =  await User.create({ name , age , email , password:hashedpass , confirm_pass, role:"user" });

  res.status(201).json({
         message: "User created successfully",
          data: {
             user,
       },});
}catch (error) {
  next(error);
}
};


const login = async(req,res,next)=>{
  try{
const {email , password}=req.body
const user =  await User.findOne({email})

if (!user) {
  return res.status(400).json({ error: "Please enter a valid email" });
  }

  const isPasswordMatched = await bcrypt.compare(password, user.password);

  if (!isPasswordMatched) {
    return res.status(400).json({ error: "Please enter correct password" });
  }

  const secretKey = process.env.JWT_SECRET || "1cb4a603ce9c60f9edfcdbe8d39050fc7f2193356a6c7ab15aacacfac68b981b6e5609d8c7134fead3840b5d62dc6efcf4beac8e35720543f7eb186397d25a03"
  const token = jwt.sign({ id: user._id }, secretKey, { expiresIn: "1d" });


  
  res.status(200).json({
    message: "Successful logging in ",
    data: {
      token,
    },
  });

}catch (error) {
  next(error);
}
};

  const getallUsers = async(req , res)=>{
    const users =await User.find()
    res.status(200).json({
      message:"Users fetched succesfully ",
      data :{ users}
    });
  }


  const getOneUser = async(req , res)=>{
    const {id} = req.params;
    const user = await User.findOne({_id:id});
    res.status(200).json({
      message:"User fetched succesfully ",
      data :{ user}
    });
  }

  const updateOneUser = async(req,res)=>{
    const {id} = req.params;
    const user = await User.findByIdAndUpdate({_id : id});
    res.status(200).json({
      message:"User updated succesfully ",
      data :{ user}
    });
  }

  const deleteOneUser = async(req , res)=>{
    const {id} = req.params;
    const user = await User.findOneAndDelete({_id : id});
    res.status(200).json({
      message:"User deleted succesfully ",
      data :{ user}
    }); 
  }

  module.exports = {
    signIn ,login, getallUsers , getOneUser , updateOneUser , deleteOneUser
  }
