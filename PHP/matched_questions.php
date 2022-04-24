<?php

// Grab User submitted information
$match_id = $_POST["match_id"];
$species = $_POST["species"];
$age = $_POST["age"];
$declawed = $_POST["declawed"];

// Create connection #servername, username, password, db 
$conn = mysqli_connect("localhost", "root@localhost", "","AnimalPicker");
// Check connection
if (!$conn) {
   die("Connection failed: " . mysqli_connect_error());
}

// database insert SQL code
$sql = "INSERT INTO `matched_questions` (`match_id`, `species`, `age`, `declawed`) VALUES ('$match_id', '$species', '$age', '$declawed')";


?>


