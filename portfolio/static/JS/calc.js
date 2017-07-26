(function() {
  "use strict";

  //entries will store values and operators
  var entries = [];

  //get elements
  var calc = document.getElementById("calculator");
  var calcScreen = calc.querySelectorAll('input')[0];

  //create operator functions to select on 'equals' press
  var operators = {
    '+': function(a, b) { return a + b },
    '-': function(a, b) { return a - b },
    '/': function(a, b) { return a / b },
    '*': function(a, b) { return a * b },
  };

  calc.addEventListener('click', function(event) {
    var element = event.target;

    /*
    Numbers keep adding to the screen until an operator is pressed
    and then the final value is added to entries.
    Where an operator is on screen and a number is then pressed, the
    operator is added to the entries.
    When equals pressed, use values and operator functions to calculate total.
    */

    if(element.tagName === 'BUTTON') {
      if(element.dataset.type === 'num' && operators.hasOwnProperty(calcScreen.value)) {
        entries.push(calcScreen.value);
        calcScreen.value = '';
        calcScreen.value += element.innerHTML;
      } else if(element.dataset.type === 'num') {
        calcScreen.value += element.innerHTML;
      }
      if(element.dataset.type === 'operator') {
        entries.push(calcScreen.value);
        calcScreen.value = element.innerHTML;
      }
      if(element.dataset.type === 'clear') {
        entries = [];
        calcScreen.value = '';
      }
      if(element.dataset.type === 'equals') {
        //push last value and set first value in calculation
        entries.push(calcScreen.value);
        var sum = parseFloat(entries[0]);

        //start loop at first operator
        for (var i = 1; i < entries.length; i++) {
          var nextNum = parseFloat(entries[i+1])
          var symbol = entries[i];

          sum = operators[symbol](sum, nextNum);
          i++;
        }

        if(isNaN(sum)) {
          calcScreen.value = "Error";
        } else {
          calcScreen.value = sum;
        }

        //reset entries
        entries = [];
      }
    }
  }, false);

  /*To do:
    Screen values should be checked to prevent multiple floating points
    that would result in an error on equals.
    Entries to display above screen as each is added.
  */

}());
