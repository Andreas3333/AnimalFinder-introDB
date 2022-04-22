<?php

// Grab User submitted information
$age = $_POST["age"];
$breed = $_POST["breed"];
$color = $_POST["color"];
$declawed = $_POST["declawed"];
$location_name = $_POST["location_name"];
$personality_statement = $_POST["personality_statement"];
$pet_id = $_POST["pet_id"];
$price_id = $_POST["price_id"];
$sex = $_POST["sex"];
$sprayed_or_neutered = $_POST["sprayed_or_neutered"];
$speices = $_POST["speices"];
$vaccination = $_POST["vaccination"];
$weight = $_POST["weight"];

// Create connection #servername, username, password, db 
$conn = mysqli_connect("localhost", "root@localhost", "","AnimalPicker");
// Check connection
if (!$conn) {
   die("Connection failed: " . mysqli_connect_error());
}

// database insert SQL code
$sql = "INSERT INTO `animals` (`age`, `breed`, `color`, `declawed`, `fldMessage`) VALUES ('0', '$txtName', '$txtEmail', '$txtPhone', '$txtMessage')";


?>


