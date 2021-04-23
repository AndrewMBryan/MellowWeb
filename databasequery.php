<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <header class="text-gray-600 body-font">
  <style>
    input{
      width: 20%;
      padding: 12px 20px;
      margin: 8px 0;
      box-sizing: border-box;
      margin-left: 30%;
      margin-right: 30%;
    }
    label{
      margin-left: 30%;
      margin-right: 30%;
    }
    p{
      margin-left: 30%;
      margin-right: 30%;
    }
  </style>

  <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
    <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-blue-500 rounded-full" viewBox="0 0 24 24">
        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
      </svg>
      <span class="ml-3 text-xl header">Mellow Flow Advertising</span>
    </a>
    <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
      <a class="mr-5 hover:text-gray-900">Home Page</a>
      <a class="mr-5 hover:text-gray-900">Dashboard</a>
      <a class="mr-5 hover:text-gray-900">Contacts</a>
      <a class="mr-5 hover:text-gray-900">Complaints</a>
      <a class="mr-5 hover:text-gray-900">View Database</a>
    </nav>

  </div>
</header>
</head>
<body>
  <?php
  // parameters for connecting to database
  $servername = "localhost";
  $username = "root";
  $password = "12AsDf!!";
  $db = "capstone";

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
</body>
</html>
