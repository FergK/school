<!DOCTYPE html>

<!--
Fergus Kelley
Assignment #4 - Part 1
CSC4370 Web Programming
-->

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fergus Kelley CSC4370 Assignment #4 - Part 1</title>

     <!--Local CSS -->
    <link href="style.css" rel="stylesheet">

  </head>
  <body>
    <div class="container">
      <h1>Fergus Kelley CSC4370 Assignment #4 - Part 1</h1>

      <div>
        <a href="source.txt">Link to the PHP source code of this page</a>
      </div>

      <hr/>

      <form action="index.php" method="post">

        <div>

          <div>
            <label for="text">Text:</label>
            <textarea id="text" name="user_text"></textarea>
          </div>

          <div>
            <label for="fontfam">Font Family:</label>
            <select id="fontfam" name="user_font">
              <option value="sans">Sans Serif</option>
              <option value="serif">Serif</option>
              <option value="curs">Cursive</option>
              <option value="fant">Fantasy</option>
              <option value="mono">Monospace</option>
            </select>
          </div>

          <div>
            <label for="fontsty">Font Style:</label>
            <select id="fontsty" name="user_style">
              <option value="default">Default</option>
              <option value="bold">Bold</option>
              <option value="underline">Underline</option>
              <option value="italic">Italic</option>
            </select>
          </div>

          <div>
            <label for="fontcol">Font Color:</label>
            <select id="fontcol" name="user_color">
              <option value="black">Black</option>
              <option value="blue">Blue</option>
              <option value="red">Red</option>
              <option value="purp">Purple</option>
            </select>
          </div>

        </div>

        <div>
          <button type="submit">Send your message</button>
        </div>

      </form>

      <hr/>

<?php
// Process the form information here

if (isset($_POST['user_text'])) { // If we have post information, display the output

$stylestring = ''; // Build a CSS string based on the drop down options

switch ( $_POST['user_font'] ) { // Font family
  case 'serif':
    $stylestring .= 'font-family: serif; ';
    break;
  case 'curs':
    $stylestring .= 'font-family: cursive; ';
    break;
  case 'fant':
    $stylestring .= 'font-family: fantasy; ';
    break;
  case 'mono':
    $stylestring .= 'font-family: monospace; ';
    break;
  case 'sans':
  default:
    $stylestring .= 'font-family: sans-serif; ';
    break;
}

switch ( $_POST['user_style'] ) { // Font style
  case 'bold':
    $stylestring .= 'font-weight: bold; ';
    break;
  case 'underline':
    $stylestring .= 'text-decoration: underline; ';
    break;
  case 'italic':
    $stylestring .= 'font-style: italic; ';
    break;
  case 'default':
  default:
    break;
}

switch ( $_POST['user_color'] ) { // Font color
  case 'blue':
    $stylestring .= 'color: #00c; ';
    break;
  case 'red':
    $stylestring .= 'color: #c00; ';
    break;
  case 'purp':
    $stylestring .= 'color: #c0c; ';
    break;
  case 'black':
  default:
    break;
}

?>

      <div>
        Output:
        <p class="output" style="<?php echo $stylestring; ?>"><?php echo htmlspecialchars($_POST['user_text']); ?></p>
      </div>

<?php
} // Only display the output if the form has been submitted
?>

    </div>
  </body>
</html>
