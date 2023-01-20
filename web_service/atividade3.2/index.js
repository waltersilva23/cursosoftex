const express = require('express');

const servidor = express();

servidor.use(express.json());

const alunos = ['Alice', 'Alan', 'Pedro'];

servidor.get('/alunos/:index', (req,res) => {
    const { index } = req.params;

    return res.json(alunos[index]);
})



servidor.listen(3030);