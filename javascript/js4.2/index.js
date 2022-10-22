const express = require('express');
const app = express();

var rotas = require('./rotas');
app.use('/', rotas);

app.listen(3333, ()=>{
    console.log('Ativando servidor...');
});



