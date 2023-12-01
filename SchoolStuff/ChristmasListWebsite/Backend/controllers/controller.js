const mysql = require('mysql2')
const asyncHandler = require('express-async-handler')

const pool = mysql.createPool({
    host:"localhost",
    user:"root",
    password:"4RocketCrimzRL!",
    connectionLimit:10
})

// pool.query('SELECT * FROM itemdatabase.items',(err,res)=>{
//     return console.log(res)
// })
const ViewList = asyncHandler(async(req,res) => {

    pool.query('SELECT * FROM itemdatabase.items',(err,rows)=>{
        if(err) throw err;
        else{
            //console.log(rows)
            res.status(200).json({results:rows}) 
        }
    })
})

const addItem = (req,res) => {
    var sql = "INSERT INTO itemdatabase.items (name,itemName,itemPrice,itemLink) values (?,?,?,?);";
    pool.query(sql,[req.body.name,req.body.itemName,Number(req.body.itemPrice),req.body.itemLink],function(err,result,fields){
        if(err) console.log("Failure when trying to insert into database");
        //console.log(result);
    })
    //console.log(req.body)
}

const removeItem = (req,res) => {
    const num = Number(req.body.num);
    if(num == -1)
    {

    }
    else{
        //console.log(num)
        var sql = "DELETE FROM itemdatabase.items WHERE num = ?"
        pool.query(sql,num,function(err,result,fields){
        if(err) throw err;
    })
    }
}

module.exports = {
    ViewList,addItem,removeItem
}