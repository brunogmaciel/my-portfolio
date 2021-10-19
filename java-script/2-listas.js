console.log(`Trabalhando com listas`);

// const salvador = `Salvador`;
// const saoPaulo = `São Paulo`;
// const rioDeJaneiro = `Rio de Janeiro`;

const listaDeDestinos = new Array(
    `Salvador`,
    `Sao Paulo`,
    `Rio de Janeiro`
);

console.log(listaDeDestinos);

const idadeComprador = 19;
const estaAcompanhada = false;
const temPassagemComprada = true;
// if (idadeComprador >= 18) {
//     console.log(`É maior de idade`);
//     listaDeDestinos.splice(1,1);
// }else if (estaAcompanhada == true) {
//     console.log(`Está acompanhada`);
//     listaDeDestinos.splice(1,1);
// }else {
//     console.log(`Menor de idade. Não posso vender`);
// }

if (idadeComprador >= 18 || estaAcompanhada == true) {
    console.log(`É maior de idade`);
    listaDeDestinos.splice(1, 1);
    console.log(listaDeDestinos);
} else {
    console.log(`Menor de idade. Não posso vender`);
}