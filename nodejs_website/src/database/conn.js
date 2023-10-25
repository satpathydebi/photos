const mongoose = require("mongoose");


//Creating a database
mongoose.connect("mongodb://localhost:27017/node_dynamic", {
    useCreateIndex:true,
    useNewUrlParser:true,
    useUnifiedTopology:true
}).then(() => {
    console.log("DB connection Success");
}).catch((error) =>{
    console.log(error);
})
