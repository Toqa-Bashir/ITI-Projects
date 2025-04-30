const restrictTo = (role) => {
    return (req, res, next) => {
      if (req.user.role !== role) {
        return res.status(403).json({ error: "You are not authorized to access this resource" });
        
      }
      next();
    };
  };
  
  module.exports = restrictTo;
  