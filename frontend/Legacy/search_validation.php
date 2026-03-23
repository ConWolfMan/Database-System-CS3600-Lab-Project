<?php
// validation code for the search form. We may not use it yet, but figured I'd get it started in case
// !!!!!!!!!!!!!! so turns out Github pages doesn't support PHP and we have to switch to something else. !!!!!!!!!!!!!!!!!


$fnameErr = $lnameErr = $phoneErr = $atLeastOneErr = "";
$fname = $lname = $phone = "";
$submitted = false;

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Only validate name if something was entered
    if (!empty($_POST["fname"])) {
        $fname = test_input($_POST["fname"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $fname)) {
            $fnameErr = "Only letters and white space allowed";
        }
    }
    
    // Only validate last name if something was entered
    if (!empty($_POST["lname"])) {
        $lname = test_input($_POST["lname"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $lname)) {
            $lnameErr = "Only letters and white space allowed";
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
    if (empty($fname) && empty($lname) && empty($phone)) {
        $atLeastOneErr = "Please enter a name or phone number to search.";
    }

    // Only flag as ready to search if no errors anywhere
    if (empty($fnameErr) && empty($lnameErr) && empty($phoneErr) && empty($atLeastOneErr)) {
        $submitted = true;
    }
}
?>