var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var urlencodedParser = bodyParser.urlencoded({ extended: true });
var cfenv = require("cfenv");

var appEnv = cfenv.getAppEnv();

let perolas = [
  "CANNON REAVES - Guri, IKIDA. 2019",
  "- Yuri, o que significa O.V.N.I? - Extraterrestre. Guri, IKIDA. 2019",
  "Lógico que existe cobra herbívora, tem cobra que come inseto... - Guguri, Ikida. 2019",
  "Cow Marx - Ikida, GURI. 2019",
  "- Yuri, o nazismo era de Direita ou de Esquerda? - Nem um nem outro. Posso estar equivocado, mas nazismo é fascismo. - IKIDA, Guri. 2019",
  "Alemões - IKIDA, Guri",
  "Urangotango - IKIDA, Guri. 2018",
  "borro de café - IKIDA, Guri. 2018",
  "Nossa, eu vou morrer de fatiga... IKIDA, Guri. 2018",
  "Terezinha é um lugar muito quente né? Terezinha que fala? - IKIDA, Guri",
  "Dava pra salvar a cidade com a quantidade de couro de jacaré que sai desse bicho - IKIDA, Guri. 2018",
  "É o crânio de um crocodilo que é mais resistente que diamante? - IKIDA, Guguri. 2018",
  "Os cara do ISIS nao sao nem louco de fazer um atestado na Rússia - IKIDA, Guri. 2018"
];

let news = [
  "Torres gêmeas são derrubadas em atentado terrorista.",
  "Dilma Rousseff sofre impeachment. Michel Temer assume presindência.",
  "Morre hoje Cazuza, ícone da música brasileira.",
  'Homem da o primeiro passo na lua: "Um pequeno passo para o homem, um grande passo para a humanidade"',
  "Apple lança iPhone: novo produto que promete mudar a forma como utilizamos o celular",
  "Brasil é derrotado por 7x1 pela seleção da Alemanha.",
  "O escândalo do Mensalão: Corrupção exposta."
];

app.get("/", function(req, res) {
  var html = "";
  html += "<body>";
  html += "<div align='center'>";
  html += "<form action='/perolas'  method='post' name='form1'>";
  html +=
    "Perola IKIDA:</p><textarea rows='4' cols='50' name='perola'></textarea><br/>";
  html += "<input type='submit' value='submit'><br/>";
  html += "<INPUT type='reset'  value='reset'>";
  html += "</form>";
  html += "</div>";
  html += "</body>";
  res.send(html);
});

app.post("/perolas", urlencodedParser, function(req, res) {
  perolas.push(req.body.perola);
  res.send(JSON.stringify(perolas));
});

app.get("/perolas", function(req, res) {
  res.send(JSON.stringify(perolas));
});

app.get("/borba_news", function(req, res) {
  res.send(JSON.stringify(news));
});

// Running Server Details.
var server = app.listen(appEnv.port, function() {
  var host = server.address().address;
  var port = server.address().port;
  console.log("Example app listening at %s:%s Port", host, port);
});
