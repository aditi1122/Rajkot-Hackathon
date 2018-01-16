?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "try1";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * from mock order by score desc limit 4";
$result = $conn->query($sql);

echo"
<style>

table {

    font-family: arial, sans-serif;

    border-collapse: collapse;

    width: 100%;

}



td, th {

    border: 10px solid #dddddd;

    text-align: left;

    padding: 10px;

}



tr:nth-child(even) {

    background-color: #dddddd;

}

</style>

";


echo "<table border='1'>
<tr>
<th>ID</th>
<th>NAME</th>
<th>SCORE</th>
</tr>";

 while($row = $result->fetch_assoc())
{
echo "<tr>";
echo "<td>" . $row["id"] . "</td>";
echo "<td>" . $row["name"] . "</td>";
echo "<td>" . $row["score"] . "</td>";
echo "</tr>";
}
echo "</table>";
$conn->close();
?>

