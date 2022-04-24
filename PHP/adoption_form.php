<?php

// Grab User submitted information
$form_id = $_POST["form_id"];
$breed = $_POST["breed"];
$residence_type = $_POST["residence_type"];
$email = $_POST["email"];
$location_name = $_POST["location_name"];
$phone_number = $_POST["phone_number"];
$customer_id = $_POST["customer_id"];
$match_id = $_POST["match_id"];

// Create connection #servername, username, password, db 
$conn = mysqli_connect("localhost", "root@localhost", "","AnimalPicker");
// Check connection
if (!$conn) {
   die("Connection failed: " . mysqli_connect_error());
}

// database insert SQL code
$sql = "INSERT INTO `adoption_form` (`form_id`, `breed`, `residence_type`, `email`, `location_name`, `phone_number`, `customer_id`, `match_id`) VALUES ('$form_id', '$breed', '$residence_type', '$email', '$location_name', '$phone_number', '$customer_id', 'match_id')";


?>


