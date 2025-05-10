const express = require("express")
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const app = express();
const helmet = require("helmet");
const mongoSanitize = require("express-mongo-sanitize");
const xss = require("xss-clean");
const hpp = require("hpp");
require("express-async-errors");
// const cors = require("cors");
const errorMiddleware = require("./middleware/errorMiddleware")
const postRouter = require("./Routers/postRouter")
const userRouter = require("./Routers/userRouter")

app.use(express.json());
app.use("/posts", postRouter);
app.use("/users",userRouter)
// app.use(cors());
dotenv.config();
app.use(errorMiddleware);
app.use(helmet());
app.use(mongoSanitize());
app.use(xss());
app.use(hpp());
app.use(limiter);


const DB_name= "Mydb";
const DB_URI =process.env.DB_URI;
const port = 3000
console.log(port)




app.listen(port,()=>{
  console.log(`Server is running on port${port}`)})


// Creating db connecting to MongonDB
mongoose.connect("mongodb://localhost:27017/Mydb").then(()=>{
   console.log("Connected to MongoDB")});
;
