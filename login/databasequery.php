<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mellow Flow Advertising</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
    #content{
      margin-left:30%;
    }
    input{
      width: 20%;
      padding: 12px 20px;
      margin: 8px 0;
      box-sizing: border-box;
    }
    </style>
    <script
        src="https://code.jquery.com/jquery-3.3.1.js"
        integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous">
    </script>
    <script>
      //loads header and footer template from separate files
    $(function(){
      $("#header").load("headers/EmployeeHeader.html");
      $("#footer").load("footers/BasicFooter.html");
    });
    </script>
    <div id="header"></div>
  </head>
<body>
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
// pull from the customers table
function selectcustomer($conn,$table,$result){
  $sql ="Select * From ".$table." Where ".$result;
  $result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  echo "<table><tr><th>ID </th><th>Name </th><th>business </th><th>website </th><th>state </th><th>phone </th><th>email </th><th>startcity </th><th>largest city </th><th>ad running </th></tr>";
  while($row = $result->fetch_assoc()) {
    echo "<tr><td>".$row["idcustomers"]."</td><td>".$row["customername"]."</td><td>"." ".$row["customerbusiness"]."</td><td>"." ".$row["customerwebsite"]."</td><td>".
    " ".$row["customerstate"]."</td><td>"." ".$row["customerphone"]."</td><td>"." ".$row["customeremail"]."</td><td>"." ".$row["customerstartcity"]."</td><td>"
    ." ".$row["customerbigcity"]."</td><td>"." ".$row["adrunning"]."</td></tr>";
  }
  echo "</table>";
} else {
  echo "0 results";
}
}
//pull from the leads table
function selectlead($conn,$table,$result){
$sql ="Select * From ".$table." Where ".$result;
$result = $conn->query($sql);

if ($result->num_rows > 0) {
// output data of each row
echo "<table><tr><th>ID </th><th>Name </th><th>stage </th><th>state </th><th>city </th><th>phone </th><th>email </th><th>website </th><th>mailing</th><th>zip </th></tr>";
while($row = $result->fetch_assoc()) {
  echo "<tr><td>".$row["idleads"]."</td><td>".$row["leadname"]."</td><td>"." ".$row["stage"]."</td><td>"." ".$row["leadstate"]."</td><td>".
  " ".$row["leadcity"]."</td><td>"." ".$row["leadphone"]."</td><td>"." ".$row["leademail"]."</td><td>"." ".$row["leadwebsite"]."</td><td>"
  ." ".$row["leadmailing"]."</td><td>"." ".$row["leadzip"]."</td></tr>";
}
echo "</table>";
} else {
echo "0 results";
}
}
// if the submit button is pressed check the input to see which table to pull from
if( isset($_GET['submit']) )
  {
      $val1 = htmlentities($_GET['table']);
      $val2 = htmlentities($_GET['result']);
      if ($val1 == "customers"){
      echo(selectcustomer($conn,$val1, $val2));
    }elseif($val1 == "leads"){
      echo(selectlead($conn,$val1, $val2));
    }else{
      echo("Invalid entry for table");
    }
  }
  ?>
  <div id= "content">
  <br>
  <p>
    Enter the Table and specific information you'd like to retrieve from the database below:
  </p>
  <br>
  <form action="" method="get">
    <label for="table">Table(customers or leads):</label><br>
    <input type="text" id="table" name="table"><br>
    <label for="result">What you want (i.e. "customername = 'Steve'"):</label><br>
    <input type="text" id="result" name="result">
    <br>
    <input type="submit" name = "submit" value="Submit">
  </form>
</div>

</body>
</html>
