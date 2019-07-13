const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());

app.get("/", (req, res) => {
  console.log(req);
  res.send({ message: "olá!" });
});

app.listen(3555, () => {
  console.log("server started!");
});
