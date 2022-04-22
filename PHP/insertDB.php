<?php

// Grab User submitted information
$ = $_POST["user"];
$ = $_POST["pass"];

// Create connection #servername, username, password, db 
$conn = mysqli_connect("localhost", "root@localhost", "","AnimalPicker");
// Check connection
if (!$conn) {
   die("Connection failed: " . mysqli_connect_error());
}

// database insert SQL code
$sql = "INSERT INTO `` (`Id`, `fldName`, `fldEmail`, `fldPhone`, `fldMessage`) VALUES ('0', '$txtName', '$txtEmail', '$txtPhone', '$txtMessage')";


?>


