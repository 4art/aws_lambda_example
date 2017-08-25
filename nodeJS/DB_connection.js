var mysql = require('mysql');


var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'root',
    database : 'security'
});


exports.get_mysql_query = function(query, callback){

    connection.query(query, function(err, result){
        if(!err){
            callback(err, result);
        }
        else{
            console.error("Can't get data from mysql");
                callback(err);
            }
        });
}
