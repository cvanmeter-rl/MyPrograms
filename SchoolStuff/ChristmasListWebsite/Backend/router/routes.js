const express = require('express');
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.json());

const {addItem,ViewList,removeItem} = require('../controllers/controller')
const routes = express.Router()

routes.get('/',ViewList)
routes.post('/addEntry',bodyParser.json(),addItem)
routes.post('/removeEntry',bodyParser.json(),removeItem)

module.exports = routes

