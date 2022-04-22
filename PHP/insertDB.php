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

echo"Conected To Data Base";

$conn->autocommit(false);
$error= array();

$a=$conn-> query("Insert into	account_info values(1099,'Sam',3450)");

if(a==false){
	array_push($error,'Problem');
}

$b=$conn-> query("Insert into	account_info values(20199,'Sabil',5550)");

if(b==false){
	array_push($error,'Problem');
}

//array_push($error,'Problem');

if(!empty($error)){
	
	$conn->rollback();
	echo "Transaction Unsuccessful!";

}
else{
	echo "Transaction Successful!";
	$conn->commit();
}
?>


