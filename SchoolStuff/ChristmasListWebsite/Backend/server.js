const express = require('express')
const app = express()
const dotenv = require('dotenv').config
const port = 8000
const mysql = require('mysql2')
const cors = require('cors')

app.use(cors())

const corsOptions = {
    origin: 'http://localhost:3000',
    allowedHeaders: ['Content-Type','Authorization']
}

app.use(cors(corsOptions))

// const pool = mysql.createPool({
//     host:"localhost",
//     user:"root",
//     password:"4RocketCrimzRL!",
//     connectionLimit:10
// })

// pool.query('SELECT * FROM itemdatabase.items',(err,res)=>{
//     return console.log(res)
// })

app.use(express.json())
app.use(express.urlencoded({extended:false}))//body parser

app.get('/',(req,res) => res.status(200).json({message:'hello'}))

app.use('/list',require('./router/routes'))

app.listen(port,() => console.log('example app listening on port ' + port + '!'))