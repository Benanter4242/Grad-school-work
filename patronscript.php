<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>LIS458 Patron Last Name Script</title>
</head>

<body>
	<h2>LIS458<br>Patron Last Name <br> Script <br>
	by Ben Jacobs</h2>
<p> Here are your results:</p>
	<hr>
	<?php
	/* Part 1 - Connect to ben.simmons.edu*/
	$host="dany.simmons.edu";
	$user="jacobb";
	$password="1940318";/* your ID # */
	$database="45801sp19_jacobb";
	mysql_connect($host,$user,$password);
	mysql_select_db($database);

	/* Part 2 the SQL query*/

	$sql=select *
  from Lizzie_card
  where Card_name=\"$_POST[last]\"";


	$result=mysql_query($sql);
	 /* Begin Part 3 - the View */

	echo("<table border=\"15px\">");
	for($i=0;$i<mysql_num_rows($result);$i++)
	{
		echo("<tr>");
		$row_arry=mysql_fetch_row($result);
		for($c=0;$c<mysqul_num_fields($result);$c++)
		{
			echo("<td>".row_array[$c]."<td>");

		}

		echo("</tr>");

	}

	echo("<table>");


	?>
	</body>
</html>
