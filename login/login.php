<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mellow Flow Advertising</title>
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="login.css">
    <script
        src="https://code.jquery.com/jquery-3.3.1.js"
        integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous">
    </script>
    <script src="../pull.js"></script>
    <script>
    $(function(){
      $("#header").load("../headers/LowerBasic.html");
      $("#footer").load("../footers/BasicFooter.html");
    });
    </script>
    <?php
    // parameters for connecting to database
    $servername = "sql111.byethost5.com";
    $username = "b5_28454471";
    $password = "AdvancedF0rLife";
    $db = "b5_28454471_mellowflow";

    // Create connection
    $conn = new mysqli($servername, $username, $password,$db);

    // Check connection
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }
    function login($conn, $user, $pass){
      $result = $mysqli->query("SELECT idemployee FROM employee WHERE employeeusername = '".$user."' AND employeepassword = '".$pass."'");
      if($result->num_rows == 1) {
        header("Location: databasequery.php");
        exit();
  } else {
    echo("Invalid username or password")
}
    }
    if( isset($_GET['submit']) )
      {
          $val1 = htmlentities($_GET['un']);
          $val2 = htmlentities($_GET['pass']);
          login($conn,val1,val2);
      }
      ?>
    <div id="header"></div>
  </head>
<div style="background-image: url('../assets/bubbles.png'); background-repeat:no-repeat; background-position:center; opacity: 0.9;" class="image-main-container" >
  <body>
    <div class="main">
      <p class="sign" align="center">Sign in</p>
      <form class="form1">
        <input name = "un" class="un " type="text" align="center" placeholder="Username">
        <input name = "pass" class="pass" type="password" align="center" placeholder="Password">
        <a name = "submit" class="submit" align="center">Sign in</a>
        <p class="forgot" align="center"><a href="#">Forgot Password?</p>


      </div>

  </body>
</div>
<!--  Footer  -->
  <div id="footer"></div>
</html>
