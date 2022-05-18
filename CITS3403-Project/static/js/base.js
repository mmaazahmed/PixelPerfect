// Creating the collapsible sidebar for guesses

$(window).on('load', () => { 
  var coll = document.getElementsByClassName("collapsible");
    var i;
    
    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
          content.style.maxHeight = null;
        } else {
          content.style.maxHeight = content.scrollHeight + "px";
        } 
      });
    }

    // Initialising required constants
    const overlay_div = document.getElementById('overlay')
    const overlay_txt = document.getElementById('overlay-text')

    const share_div = document.getElementById('share')
    const share_txt = document.getElementById('share-text')

    const thanks_div = document.getElementById('thanks')
    const thanks_txt = document.getElementById('thanks-text')

    const button = document.getElementById('share-button')

    const outcome_div = document.getElementById('outcome');
    const outcome_txt = document.getElementById('outcome-text');

// Code blocks to stop the div from disappearing when clicking in the text field, but to disappear when clicking outside the field.
    share_div.addEventListener("click", function () {
      $('#share').fadeOut(100);
    }, false);
    share_txt.addEventListener("click", function (ev) {
     ev.stopPropagation();
  }, false);

    $(overlay_div).click(function(){
      $('#overlay').fadeOut(100)
    })
    overlay_txt.addEventListener("click", function (ev) {
     ev.stopPropagation();
  }, false);

    $(thanks_div).click(function(){
      $('#thanks').fadeOut(100)
    })
    thanks_txt.addEventListener("click", function (ev) {
     ev.stopPropagation();
  }, false);

    outcome_div.addEventListener("click", function () {
      $('#outcome').fadeOut(100);
    }, false);

    outcome_txt.addEventListener("click", function (ev) {
       ev.stopPropagation();
    }, false);


    // JS to add guesses to sidebar and to check for correct answer.
    guess = document.getElementById('guesstxt');

    var guess_copyandpaste = 'Play Pixel Perfect: A Game by Sean, Maaz, Pablo and Cameron: \n'

    var correct_answer = 'test'

    guess.addEventListener("keypress", function(e){
      if (e.key === 'Enter') {
        let count = document.getElementById('guess-content').children.length + 1;
        guesstxt = $(guess).val();
        guess_correct = Boolean(guesstxt == correct_answer)
        console.log(guess_correct)
        if (guess_correct) {
          guess_copyandpaste = guess_copyandpaste + 'GUESS ' + String(count) + ': CORRECT! 😁' + '\n'
          onOutcome(true, count, correct_answer)
        }
        else if (guess_correct == false && count < 5) {
          guess_copyandpaste = guess_copyandpaste + 'GUESS ' + String(count) + ': INCORRECT 😭' + '\n'
        }
        else {
          guess_copyandpaste = guess_copyandpaste + 'GUESS ' + String(count) + ': INCORRECT 😭' + '\n'
          onOutcome(false, count, correct_answer)
        }
        $('#guess-content').append("<p class = 'guess'>" + 'GUESS ' + String(count) + ': ' + guesstxt + "</p>")
        $(guess).val('')
      }
      
    })

    // When the share button is clicked, copy the share text to clipboard.
    button.addEventListener('click', function(){
      document.getElementById("share-button").innerHTML = "Copied to Clipboard!";
      navigator.clipboard.writeText(guess_copyandpaste)
    })

});



// Function to turn on the overlays when buttons at the top are clicked (Or when the user runs out of guesses/gets the correct answer.)
function onRules() {
  document.getElementById("overlay").className = 'fade-in';
  document.getElementById("overlay").style.display = "block";
}

function onShare() {
  document.getElementById("share").className = 'fade-in';
  document.getElementById("share").style.display = "block";
}

function onThanks() {
  document.getElementById("thanks").className = 'fade-in';
  document.getElementById("thanks").style.display = "block";
}

function onOutcome(bool, count, correct_answer) {
document.getElementById("outcome").className = 'fade-in';
document.getElementById("outcome").style.display = "block";
if (bool == true) {
  document.getElementById('outcome-title').innerHTML = 'You Win!';
  document.getElementById('guess-count').innerHTML = count
} else {
  document.getElementById('outcome-title').innerHTML = 'You Lose!'
  document.getElementById('outcome-eval').innerHTML = 'The correct answer was ' + correct_answer + '.';

};
}

  // Code to create countdown timer for each new day - Will add functionality of updating fields in the future.
  var tomorrow = new Date()

  // add 1 day to today
  tomorrow.setDate(new Date().getDate() + 1)
  tomorrow.setHours(0,0,0)
  console.log(tomorrow)

  // Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  now = new Date()
    
  // Find the distance between now and the count down date
  var distance = tomorrow - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("countdown-timer").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown-timer").innerHTML = "EXPIRED - Please refresh the page.";
  }
}, 1000);