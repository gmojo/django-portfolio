(function() {
    "use strict";

    var game = document.getElementById("responseBtns");
    var gameBtns = game.getElementsByTagName("button");
    var outcome = document.getElementById("outcome");
    var modeSwitch = document.getElementById("modeSwitch");
    var countScreen = document.getElementById("counter");

    var simon = {
        sequence: [], //game sequence of buttons
        strictMode: false,
        counter: 1, //count number in sequence
        playerTurn: false, //control player input
        playerAttempt: [], //player sequence; reset after each failed attempt and win
        index: 0, //for checking playerAttempt against sequence
        sounds: {
            'red': new Audio("https://s3.amazonaws.com/freecodecamp/simonSound1.mp3"),
            'green': new Audio("https://s3.amazonaws.com/freecodecamp/simonSound2.mp3"),
            'blue': new Audio("https://s3.amazonaws.com/freecodecamp/simonSound3.mp3"),
            'yellow': new Audio("https://s3.amazonaws.com/freecodecamp/simonSound4.mp3")
        },
        selectRandom: function() {
            //create array from nodeList and return random box
            var btnsArr = Array.prototype.slice.call(gameBtns);
            return btnsArr[Math.floor(Math.random() * btnsArr.length)];
        },
        startGame: function() {
            //clear all properties and highlight first item
            simon.resetGame();

            simon.sequence.push(simon.selectRandom());
            view.showPattern();

            countScreen.value = simon.counter;
            simon.playerTurn = true;
        },
        resetGame: function() {
            //clear all object properties and text on screen
            countScreen.value = 0;
            simon.counter = 1;
            simon.playerTurn = false;
            simon.playerAttempt = [];
            simon.sequence = [];
            simon.index = 0;
            outcome.innerHTML = "";
        },
        setupActionBtns: function() {
            //register click events for start/reset
            var startBtn = document.getElementById('start');
            var resetBtn = document.getElementById('reset');

            startBtn.onclick = simon.startGame;
            resetBtn.onclick = simon.resetGame;

            //update strict mode when toggle button changed
            modeSwitch.onchange = function() {
                if (modeSwitch.checked === true) {
                    simon.strictMode = true;
                } else {
                    simon.strictMode = false;
                }
            };
        }
    };

    //view object to manage visualisations in game
    var view = {
        highlightItem: function(item) {
            //style button, play sound and wait 0.5 seconds before clearing
            item.style.backgroundColor = item.className;
            simon.sounds[item.className].play();

            setTimeout(function() {
                item.style.backgroundColor = "";
            }, 500)
        },
        showPattern: function() {
            //loop through sequence and pass each item to highlightItem
            //wait 1 second before initiating and then 0.8 seconds between each item passed
            setTimeout(function() {
                for (var i = 0; i < simon.sequence.length; i++) {
                    setDelay(i);
                }

                function setDelay(i) {
                    setTimeout(function() {
                        view.highlightItem(simon.sequence[i]);
                    }, i * 800)
                }
                outcome.innerHTML = "";
            }, 1000)
        }
    };

    game.addEventListener('click', function(event) {
        //only repond to click events on buttons when it is the players turn
        if (simon.playerTurn) {
            simon.playerAttempt.push(event.target);
            simon.sounds[event.target.className].play();

            //if guess is incorrect try again; differnt outcomes for strict/non-strict
            if (simon.playerAttempt[simon.index] !== simon.sequence[simon.index]) {
                simon.playerTurn = false;
                if (simon.strictMode) {
                    outcome.innerHTML = "You lose, start again!";
                } else {
                    outcome.innerHTML = "Incorrect, try again!";
                    simon.playerAttempt = [];
                    simon.index = 0;

                    view.showPattern();
                    simon.playerTurn = true;
                }
            }
            //if not wrong
            else {
                //if end of playerAttempt/sequence
                if (simon.index === simon.sequence.length - 1) {
                    simon.playerTurn = false;
                    simon.playerAttempt = [];
                    simon.counter++;

                    //if more than 20 in sequence then player wins
                    if (simon.counter === 21) {
                        outcome.innerHTML = "You win!";
                    } else {
                        //next level; reset index and add new item to sequence
                        countScreen.value = simon.counter;
                        simon.index = 0;

                        simon.sequence.push(simon.selectRandom());
                        view.showPattern();
                        simon.playerTurn = true;
                    }
                }
                //if not end of playerAttempt/sequence then increase index and test on next click
                else if (simon.index !== simon.sequence.length - 1) {
                    simon.index++
                        simon.playerTurn = true;
                    return;
                }
            }
        }
    }, false) //end event listener

    simon.setupActionBtns();

})();