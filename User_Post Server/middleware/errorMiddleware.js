
// importing APIErrors
const APIError =require("../utilis/APIErrors")

const errorMiddleware = (err, req, res, next) => {
    
    console.error(err.stack);
  
    // CastError
    if (err.name === "CastError") {
      res.status(400).json({ message: "Invalid ID" });
    }
    // validation error
    if (err.name === "ValidationError") {
      res.status(400).json({ message: "Invalid Data" });
    }
     // duplicate key error
  if (err.code === 11000) {
    const field = Object.keys(err.keyPattern)[0];
    return res.status(400).json({
      message: `Duplicate value for ${field}`,
    });
  }

  // catching thrown errors by APIError
  if (err instanceof APIError) {
    res.status(err.statusCode).json({
      message: err.message,
    });
  }

  // catching any other errors
  res.status(500).json({
    message: "An unexpected error occurred",
    error: err.message,
  });

  // handle jwt errors
  if (err.name === "JsonWebTokenError") {
    return res.status(401).json({ message: "Unauthorized" });
  }

};

module.exports = errorMiddleware;