function getNewNumber() {
    return Math.floor(Math.random() * 100) + 1;
}

var theNumber = getNewNumber();
var triesRemaining = 7;

function guess() {

  // Get the elements we need
  var guessField = document.getElementById('guessField');
  var result = document.getElementById('result');

  // Get the user's guess from the field
  var theGuess = parseInt(guessField.value, 10);

  // Change the message depending on the result
  if ( theGuess > theNumber ) {
    result.innerHTML = "<br />Your guess is too high!<br/>" + triesRemaining + " tries remaining";
    triesRemaining--;
  } else if ( theGuess < theNumber ) {
    result.innerHTML = "<br />Your guess is too low!<br/>" + triesRemaining + " tries remaining";
    triesRemaining--;
  } else {
    result.innerHTML = "<br />That's right! The number was " + theNumber + "!<br /> A new number has been picked!";
    theNumber = getNewNumber();
    triesRemaining = 7;
  }

}
