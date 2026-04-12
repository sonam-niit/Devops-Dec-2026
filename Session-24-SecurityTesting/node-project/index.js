const express = require('express')

const app= express()//creating server

const password='admin123' //Hardcoded cred

app.get('/',(req,res)=>{
    eval("console.log('Testing')") //eval statement
    res.send("Hello From SonarQube")
    console.log("Hello From SonarQube")
    //Duplicate statement
})

//start server
app.listen(3000,()=>console.log("Server Started"))