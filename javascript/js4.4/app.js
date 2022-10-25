const express = require('express');
const app = express();

const db = require('./models/db');

app.get("/", async (req, res) =>{
    res.send("Página inicial");
});

app.listen(3333, ()=>{
    console.log("Ativando servidor... http://loacalhost:3333")
});
