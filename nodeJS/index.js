'use strict'
var DB = require('./DB_connection.js');


function getProductByID(id, callback){
    DB.get_mysql_query("SELECT * FROM products WHERE id = " + id, function(err, result){
        if(!err){
            if(result.length > 0){
                callback(err, result);
            }
            else{
                DB.get_mysql_query("SELECT * FROM products", function(err, result){
                    if(!err){
                        callback(err, result);
                    }
                });
            }
        }
    });
}

exports.handler = (event, context, callback) => {
    getProductByID(event.id, function(err, result){
        if(!err)
            callback(null, result);
    });
}

exports.handler({id: 44}, null, function(err, result){
    console.log(result);
});