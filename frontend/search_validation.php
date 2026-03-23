<?php
// validation code for the search form. We may not use it yet, but figured I'd get it started in case

$nameErr = $phoneErr = $atLeastOneErr = "";
$name = $phone = "";
$submitted = false;

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Only validate name if something was entered
    if (!empty($_POST["name"])) {
        $name = test_input($_POST["name"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
            $nameErr = "Only letters and white space allowed";
        }
    }

    // Only validate phone if something was entered
    if (!empty($_POST["phone"])) {
        $phone = test_input($_POST["phone"]);
        if (!preg_match("/^\d{3}-\d{3}-\d{4}$/", $phone)) {
            $phoneErr = "Invalid phone number format. Use XXX-XXX-XXXX.";
        }
    }

    // Check at least one field was filled
    if (empty($name) && empty($phone)) {
        $atLeastOneErr = "Please enter a name or phone number to search.";
    }

    // Only flag as ready to search if no errors anywhere
    if (empty($nameErr) && empty($phoneErr) && empty($atLeastOneErr)) {
        $submitted = true;
    }
}
?>