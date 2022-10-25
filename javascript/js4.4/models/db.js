const Sequelize = require('sequelize');

const sequelize = new Sequelize("softex", "walter", "123456", {
    host: 'localhost',
    dialect: 'mysql'
});

sequelize.authenticate()
.then(function(){
    console.log("Conexão com o banco de dados realizada com sucesso!");
}).catch(function(){
    console.log("Erro: conexão com o banco de dados não realizada com sucessor!");
});

//21:44

module.exports = sequelize;