const express = require('express')

const app= express()//creating server

app.get('/',(req,res)=>{
    res.send("Hello From SonarQube")
})

//start server
app.listen(3000,()=>console.log("Server Started"))