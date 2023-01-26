const { consultarCep } = require("correios-brasil");

// Cep pode ser String ou Number
const cep = "55644010"; // 21770200 , '21770-200', '21770 200'.... qualquer um formato serve

consultarCep(cep).then((response) => {
  console.log(response);
});
