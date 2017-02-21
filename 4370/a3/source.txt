<!DOCTYPE html>

<!--
Fergus Kelley
Assignment #3
CSC4370 Web Programming
-->

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fergus Kelley CSC4370 Assignment #3</title>

     <!--Local CSS -->
    <link href="style.css" rel="stylesheet">

  </head>
  <body>
    <h1>Fergus Kelley CSC4370 Assignment #3</h1>

    <div>
      <a href="source.txt">Link to the PHP source code of this page</a>
    </div>

    <hr>
    <h2>Part 1</h2>
    <?php
    function isBitten() {
      $heAteMyLunch = rand(0,1);
      if ($heAteMyLunch == 0) {
        print('Charlie ate my lunch!');
      } else {
        print('Charlie did not eat my lunch!');
      }
    }
    ?>

    <p><?php isBitten(); ?></p>

    <hr>
    <h2>Part 2</h2>

    <table id="checkerboard"><?php

    $redcell = false;

    for ($i=0; $i < 8; $i++) {
      print("\n      <tr>\n");
      for ($j=0; $j < 8; $j++) {

        print("        <td class=\"checkercell ");

        $redcell = !$redcell;

        if ( $redcell ) {
          print("redcell");
        } else {
          print("blackcell");
        }

        print("\"></td>\n");

      }
      $redcell = !$redcell;
      print("      </tr>");
    }

    ?>

    </table>

    <hr>
    <h2>Part 3</h2>

    <?php
    $month = array ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');

    print("Original array printed with a for loop: ");
    for ($i=0; $i < count($month); $i++) {
      print( $month[$i] . ' ' );
    }

    print("<br/><br/>\n");

    sort($month);

    print("Sorted array printed with a for loop: ");
    for ($i=0; $i < count($month); $i++) {
      print( $month[$i] . ' ' );
    }

    print("<br/><br/>\n");

    $month = array ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');

    print("Original array printed with a foreach loop: ");
    foreach ($month as $value) {
      print( $value . ' ' );
    }

    print("<br/><br/>\n");

    sort($month);

    print("Sorted array printed with a foreach loop: ");
    foreach ($month as $value) {
      print( $value . ' ' );
    }

    ?>

    <hr>
    <h2>Part 4</h2>

    <?php

    $restaurants = array(
      "Chama Gaucha" => 40.5,
      "Aviva by Kameel" => 15,
      "Bone's Restaurant" => 65,
      "Umi Sushi Buckhead" => 40.5,
      "Fandangles" => 30,
      "Capital Grille" => 60.5,
      "Canoe" => 35.5,
      "One Flew South" => 21,
      "Fox Bros. BBQ" => 15,
      "South City Kitchen Midtown" => 29,
    );

    function printRestaurants( $restaurantList) {
      print("<table class=\"restaurantTable\">\n");
      foreach ($restaurantList as $name => $price) {
        print( '<tr><td>' . $name . '</td><td>' . number_format($price, 2, '.', '') . '</td></tr>' . "\n" );
      }
      print("</table><br/>\n");
    }

    print("The 10 Best Restaurants in Atlanta: ");
    printRestaurants( $restaurants );

    print("The 10 Best Restaurants in Atlanta (sorted by name): ");
    ksort($restaurants);
    printRestaurants( $restaurants );

    print("The 10 Best Restaurants in Atlanta (sorted by average cost): ");
    asort($restaurants);
    printRestaurants( $restaurants );



    ?>

  </body>
</html>
