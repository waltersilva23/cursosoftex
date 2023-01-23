const express = require('express');

const servidor = express();

servidor.use(express.json());

const alunos = ['Alice', 'Alan', 'Pedro'];

//Retorna um aluno
servidor.get('/alunos/:index', (req,res) => {
    const { index } = req.params;

    return res.json(alunos[index]);
});

//Retorna todos os alunos
servidor.get('/alunos', (req,res) => {
    return res.json(alunos)
});

//Adiciona um novo aluno
servidor.post('/alunos', (req,res) => {
    const { nome } = req.body;
    alunos.push(nome);

    return res.json(alunos);
});

//Atualizar a lista de alunos
servidor.put('/alunos/:index', (req,res) => {
    const { index } = req.params;
    const { nome } = req.body;

    alunos[index] = nome;
    return res.json(alunos);
});

//Excluir aluno da lista
servidor.delete('/alunos/:index', (req,res) => {
    const { index } = req.params;

    alunos.splice(index, 1);
    return res.json({ message: "O aluno foi excluido da lista"});
});

//rotas
//GET /alunos/:index e /alunos
//POST /alunos
//PUT /alunos/:index
//DELETE /alunos/:index

//STATUS HTTP: Todas tiveram o status 200.



servidor.listen(3030);