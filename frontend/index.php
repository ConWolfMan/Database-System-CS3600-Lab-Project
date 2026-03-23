<?php require 'search_validation.php'; ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Online Phone Book</title>


    <!--Note, load bootsrap first or it'll override some of the styling from the css file-->
    <!-- Enabling bootstrap for forms stuff -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- This links to the my_style.css file so that we can apply its styling -->
    <link rel="stylesheet" href="my_style.css">


</head>
<body>
    <!-- Top header navbar -->
    <nav class="navbar">
        <a href="index.html" class="nav-link">Home</a> <!-- ! note to team : These are just temp examples, change in the future !  -->
        <a href="browse_contacts.html" class="nav-link">Browse Contacts</a>
        <a href="add_contact.html" class="nav-link">Add Contact</a>
        <a href="delete_contact.html" class="nav-link">Delete Contact</a>
    </nav>

    <!-- hero / header -->
    <header class="hero">
        <h1>Online Phone Book Database</h1>
        <h3>Find contacts in our database</h3>
    </header>


    <!-- main content -->
    <div class="content-panel">
        <p>
            Stuff and things
        </p>
    </div>
  
    <div class="content-panel">
    <h2>Search</h2>
    <div class="form-content">
        <form>

            <h3></h3>
            <!-- Name row -->
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label class="form-label" for="first_name">First Name</label>
                            <input class="form-input" type="text" id="first_name" name="first_name" placeholder="First name">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <label class="form-label" for="last_name">Last Name</label>
                            <input class="form-input" type="text" id="last_name" name="last_name" placeholder="Last name">
                    </div>
                </div>
            </div>

            <!-- Phone number row -->
            <div class="row">
                <div class="col-12">
                    <div class="form-group">
                        <label class="form-label" for="phone">Phone Number</label>
                            <input class="form-input" type="text" id="phone" name="phone" placeholder="XXX-XXX-XXXX">
                    </div>
                </div>
            </div>


            <!-- Buttons -->
            <div class="form-actions">
                <button type="submit" class="btn btn-primary">Search</button>
                <button type="reset" class="btn btn-secondary">Reset</button>
            </div>

        </form>
    </div>
</div>

     <!-- Bottom footer navbar -->
    <footer class="footer"> <!-- ! Note to team, these pages do not exist yet, we'll probably need to make them soon ! -->
        <p>
            &copy; 2026 "Online Phone Book Database". All rights reserved.
                &nbsp;|&nbsp;
                <a href="cookie_policy.html">Cookie Policy</a>
                &nbsp;|&nbsp;
                    <a href="privacy_policy.html">Privacy Policy</a>
                &nbsp;|&nbsp;
                    <a href="terms_and_cond.html">Terms and Conditions</a>
        </p>
    </footer>
</body>

</html>