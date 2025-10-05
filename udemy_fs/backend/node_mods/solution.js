const fs = require("fs");
const { fileURLToPath } = require("url");

const fileContent = "Hello Node"; 

fs.writeFile("message.txt", fileContent, (err) => {
  if (err) throw err;
  console.log("The file has been saved!");
});

fs.readFile("message.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});


/* 

Use:

import { randomSuperhero } from "superheroes";
const name = randomSuperhero();

Instead of:

import superheroes from "superheroes";
const name = superheroes.random();

*/ 