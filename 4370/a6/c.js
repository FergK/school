var grid = [];
var state = 'waitingForStart';
var matches = 0;

var memorizationTime;
var memorizationTimer;
var gameTime;
var gameTimer;
var clickTimer;

var numPics;

function Picture(image) {
  this.matched = false;
  this.image = image;
};

var selected  = { i: null, j: null };

function start() {

  // Get the elements we need
  var instructions = document.getElementById('instructions');
  var matchTable = document.getElementById('matchTable');
  var picSelect = document.getElementById('picSelect');
  var secsSelect = document.getElementById('secsSelect');

  // Get the values from the select boxes
  numPics = picSelect.value;
  memorizationTime = secsSelect.value;
  gameTime = numPics * 15;

  // Generate a list of the photos to use
  var picList = [];
  for (var i = 1; i <= numPics; i++) {
    picList.push( new Picture("pics/" + i + ".gif") );
    picList.push( new Picture("pics/" + i + ".gif") );
  }

  // Create the grid by randomly pulling elements from the list
  // and populate the match table with the pictures
  for (var i = 0; i < 4; i++) {
    grid[i] = [];
    var newRow = matchTable.insertRow();
    for (var j = 0; j < (numPics / 2); j++) {
      grid[i][j] = picList.splice(Math.floor(Math.random() * picList.length), 1)[0];
      var newCell = newRow.insertCell(0);
      newCell.innerHTML = '<img src="' + grid[i][j].image + '" id="' + i + j + '" onclick="picClicked(' + i + ',' + j + ')" />';
    }
  }

  // Hide the instructions
  instructions.style.display = 'none';

  // Change the state and start the memorization timer
  state = 'memorization';
  timerText.innerHTML = "Memorization time left: " + memorizationTime;
  memorizationTimer = window.setInterval(memorizationTick, 1000);
}

function memorizationTick() {
  memorizationTime--;

  var timerText = document.getElementById('timerText');
  timerText.innerHTML = "Memorization time left: " + memorizationTime;

  if ( memorizationTime == 0 ) {
    // Times up, starting play
    window.clearInterval(memorizationTimer);
    beginPlay();
  }
}

function beginPlay() {

  // Hide the cards
  hideImages();

  // Change the state and start the game timer
  state = 'waitingForClick';
  timerText.innerHTML = "Time left: " + gameTime;
  gameTimer = window.setInterval(gameTick, 1000);

}

function gameTick() {
  gameTime--;

  var timerText = document.getElementById('timerText');
  timerText.innerHTML = "Time left: " + gameTime;

  if ( gameTime <= 0 ) {
    lose();
  }
}

function hideImages() {
  for (var i in grid) {
    for (var j in grid[i]) {
      if ( !grid[i][j].matched ) {
        var image = document.getElementById(''+i+j);
        image.src = 'pics/blank.gif';
      }
    }
  }
}

function picClicked(i, j) {

  if ( state == 'waitingForClick' ) {
    // User is selecting the first image of the pair, mark it as selected
    state = 'image1Selected';
    selected.i = i;
    selected.j = j;
    var image = document.getElementById(''+i+j);
    image.src = grid[i][j].image;

  } else if ( state == 'image1Selected' ) {
    // User is selecting the first image of the pair, compare it to the first

    state = 'image2Selected';
    var image = document.getElementById(''+i+j);
    image.src = grid[i][j].image;

    if ( grid[i][j].image == grid[selected.i][selected.j].image ) {
      // They match! Mark them as matched and
      grid[i][j].matched = true;
      grid[selected.i][selected.j].matched = true;
      selected.i = null;
      selected.j = null;
      matches++;

      if ( matches == numPics ) {
        // All the matches have been made, player wins!
        win();
      }

      state = 'waitingForClick'
    } else {
      // Incorrect match, set a timer to delay until the user can click again
      state = 'incorrectMatch';
      clickTimer = window.setTimeout(incorrectMatch, 3000)
    }

  }

}

function incorrectMatch() {
  hideImages();
  state = 'waitingForClick';
}

function win() {
  state = 'waitingForStart';
  window.clearInterval(gameTimer);
  window.clearTimeout(incorrectMatch)
  var timerText = document.getElementById('timerText');
  timerText.innerHTML = "YOU WON IN " + gameTime + " SECONDS!!! <a href='c.html'>Play again?</a>";
}

function lose() {
  state = 'waitingForStart';
  window.clearInterval(gameTimer);
  window.clearTimeout(incorrectMatch)
  var timerText = document.getElementById('timerText');
  timerText.innerHTML = "YOU LOSE :( <a href='c.html'>Play again?</a>";
}
