<!DOCTYPE html>

<!--
Fergus Kelley
Assignment #4 - Part 2
CSC4370 Web Programming
-->

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fergus Kelley CSC4370 Assignment #4 - Part 2</title>

     <!--Local CSS -->
    <link href="calendar.css" rel="stylesheet">

  </head>
  <body>
    <div class="container">
      <h1>Fergus Kelley CSC4370 Assignment #4 - Part 2</h1>

      <div>
        <a href="calendar.txt">Link to the PHP source code of this page</a>
      </div>
      <div>
        <a href="https://validator.w3.org/nu/?doc=http%3A%2F%2Fcodd.cs.gsu.edu%2F~fkelley2%2Fa4%2Fp2%2F">Link to the HTML validation for this page</a>
      </div>

      <hr/>

<?php

  date_default_timezone_set('America/New_York');

  $thistime = time();
  echo '<h2>Calendar - ' . date('g:i a') . ' on ' . date('F j, Y') . '</h2>';

  $hours_to_show = 12; // The number of rows to show

  function get_hour_string( $timestamp ) {
    return date('g a', $timestamp );
  }

?>

      <table class="calendar">
        <tr class="calhead">
          <td>Hour</td>
          <td>Charlie</td>
          <td>Dee</td>
          <td>Mac</td>
          <td>Dennis</td>
          <td>Frank</td>
        </tr>

<?php
  for ($i=0; $i < $hours_to_show; $i++) {
?>

        <tr>
          <td class="hourcol"><?php

          echo get_hour_string($thistime);
          $thistime += 3600; // increment the time by 1 hour (60 minutes * 60 seconds)

          ?></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>

<?php
  }
?>

      </table>
    </div>
  </body>
</html>
