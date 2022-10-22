var express = require('express');
var rota = express.Router();
 
rota.get('/users', function(req, res) {
    res.send(`Listar usuários`);
});
 
rota.post('/user', function(req, res) {
    res.send(`Criar um usuário`);
});
 
module.exports = rota;