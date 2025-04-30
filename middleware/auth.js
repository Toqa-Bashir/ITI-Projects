const User = require("../Models/userModel")
const util = require("util");
const jwt = require("jsonwebtoken");
const APIError = require("./../utilis/APIErrors")

const jwtVerify = util.promisify(jwt.verify);

const auth = async(req , res , next)=>{
    try {
        const bearerToken = req.headers.authorization;
    if (!bearerToken || !bearerToken.startsWith("Bearer ")) {
      return res.status(401).json({ error: "Unauthorized, token is required" });
    }

    const token = bearerToken.split(" ")[1];

    const secretKey = process.env.JWT_SECRET;
    if (!secretKey) {
      return res.status(500).json({ error: "Internal server error, missing JWT_SECRET" });
    }
    const decodedData = await jwtVerify(token, secretKey);

    const user = await User.findById(decodedData.id).select("name email role");
    if (!user) {
      return res.status(401).json({ error: "Unauthorized, user not found" });
    }
    req.user = user ; 
    next()
    }
    catch (error) {
        return res.status(401).json({ error: "Invalid token or unauthorized" });
      }
    };
    module.exports = auth;