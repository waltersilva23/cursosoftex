const curso = ["s", "o", "f", "t", "e", "x"];

const pokemon = {
    Nome: 'Snorlax',
    Tipo: 'Normal',
    Fraqueza: 'Lutador'
}

function estudo(){
    console.log("\nQue curso estou fazendo agora?");
    for (const e of curso) {
        console.log(e);
    }
}

function pokedex(){
    console.log("\nDados do pokémon encontrado:\n")
    for (const index in pokemon){
        console.log(`${index} : ${pokemon[index]}`)
    }
}

estudo()

pokedex()
