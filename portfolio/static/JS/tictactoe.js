(function() {
  "use strict";

  var game = document.getElementById("game");
  var btns = game.getElementsByTagName("button");
  var outcome = document.getElementById("outcome");
  var playerSwitch = document.getElementById("player-switch");

  var player = "X";
  var computer = "O";
  var completedCount = 1;

  playerSwitch.onchange = function() {
    if(playerSwitch.checked === true){
      player = "O";
      computer = "X";
    } else {
      player = "X";
      computer = "O";
    }
  };

  var winningCombos = [
    [btns[0], btns[1], btns[2]],
    [btns[3], btns[4], btns[5]],
    [btns[6], btns[7], btns[8]],
    [btns[0], btns[3], btns[6]],
    [btns[1], btns[4], btns[7]],
    [btns[2], btns[5], btns[8]],
    [btns[0], btns[4], btns[8]],
    [btns[2], btns[4], btns[6]],
  ];

  //go through winningCombos to check if items in individual arrays are equal
  var winCheck = function() {

    //create inner function to check items in array are equal
    var isEqual = function(arr) {
      for(var i = 0; i < arr.length; i++) {
        if(arr[i].innerHTML !== arr[0].innerHTML || arr[i].innerHTML === '')
          return false;
      }
      return true;
    };

    //check if any arrays contain same values if so return btns for formatting
    for(var i = 0; i < winningCombos.length; i++) {
      if(isEqual(winningCombos[i])) {
        return winningCombos[i];
      }
    }

    return false;
  };//end winCheck

  //get random empty button
  var getRandBtn = function() {
    //create array from nodeList then filter for only empty btns
    var btnsArr = Array.prototype.slice.call(btns);
    var remainingBoxes = btnsArr.filter(function(btn) {
      return btn.innerHTML === '';
    })

    //return random empty box
    return remainingBoxes[Math.floor(Math.random()*remainingBoxes.length)];
  };

  //reset all buttons except reset (length-1 as reset is last button is nodeList)
  var reset = function() {
    for(var i = 0; i < btns.length-1; i++) {
        btns[i].innerHTML = '';
        outcome.innerHTML = '';
        btns[i].classList.remove('win');
        btns[i].classList.remove('lose');
        btns[i].disabled = false;
    }
    playerSwitch.disabled = false;
    completedCount = 1;
  };

  game.addEventListener('click', function(event) {
    var element = event.target;

    //Clear screen if reset button clicked or else continue with game
    if(element.classList.contains('clearBtn')) { reset(); }
    else if(element.tagName === "BUTTON"  && element.innerHTML === '') {
      element.innerHTML = player;
      element.disabled = true;
      completedCount++;
      playerSwitch.disabled = true;

      //if not won then computer has turn and wincheck run again

      if(winCheck()) {
        var result = winCheck();

        for(var i = 0; i < result.length; i++) {
          result[i].classList.add('win');
        }

        outcome.innerHTML = 'You win!';
      }
      else if(completedCount === btns.length){
        outcome.innerHTML = 'Draw! Try again.';
      }
      else if(!winCheck()) {
        getRandBtn().innerHTML = computer;
        completedCount++;

        if(winCheck()) {
          var result = winCheck();

          for(var i = 0; i < result.length; i++) {
            result[i].classList.add('lose');
          }

          outcome.innerHTML = 'You lose!';
        }
        else if(completedCount === btns.length) {
          outcome.innerHTML = 'Draw! Try again.';
        }
      }
    }
  }, false); //end event listener function

}());
