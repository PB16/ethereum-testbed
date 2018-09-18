<?php
function dbConnect() {
    $host = 'localhost';
    $port = '9000';
    $db = 'auth';
    $user = 'kasper_wissing';
    $pw = '123456';

    try{
        return new PDO("mysql:host=".$host.";dbname=".$db.";port=".$port."", $user, $pw);
        //return new PDO("mysql:host=localhost;dbname=auth;port=9000", $user, $pw);
    }
    catch(PDOException $e){
        echo $e->getMessage();
        exit;
    }

}
