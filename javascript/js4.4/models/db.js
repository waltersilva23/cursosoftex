const Sequelize = require('sequelize');

const conexao = new Sequelize("softex", "root", "123456", {
    host: 'localhost',
    dialect: 'mysql'
});

conexao.authenticate()
.then(function(){
    console.log("Conexão com o banco de dados realizada com sucesso!");
}).catch(function(){
    console.log("Erro: conexão com o banco de dados não realizada!");
});

module.exports = conexao;