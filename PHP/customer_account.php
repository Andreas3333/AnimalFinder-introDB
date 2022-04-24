<?php

// Grab User submitted information
$customer_id = $_POST["customer_id"];
$street = $_POST["street"];
$city = $_POST["city"];
$zip = $_POST["zip"];
$balance = $_POST["balance"];
$first_name = $_POST["first_name"];
$last_name = $_POST["last_name"];


// Create connection #servername, username, password, db 
$conn = mysqli_connect("localhost", "root@localhost", "","AnimalPicker");
// Check connection
if (!$conn) {
   die("Connection failed: " . mysqli_connect_error());
}

// database insert SQL code
$sql = "INSERT INTO `customer_account` (`customer_id`, `street`, `city`, `zip`, `balance`, `first_name`, `last_name`) VALUES ('$customer_id', '$street', '$city', '$zip', '$balance', 'first_name', 'last_name')";


?>


