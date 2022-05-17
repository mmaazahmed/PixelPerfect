// Creating the collapsible sidebar for guesses

$(window).on('load', () => { 
    var coll = document.getElementsByClassName("collapsible");
      console.log(coll)
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
      const overlay = document.getElementById('overlay')
      const share = document.getElementById('share')
      const thanks = document.getElementById('thanks')


      $(share).click(function(){
        $('#share').fadeOut(100)
      })

      $(overlay).click(function(){
        $('#overlay').fadeOut(100)
      })

      $(thanks).click(function(){
        $('#thanks').fadeOut(100)
      })

      guess = document.getElementById('guesstxt');

      var guess_copyandpaste = 'Play Pixel Perfect: A Game by Sean, Maaz, Pablo and Cameron: \n'

      guess.addEventListener("keypress", function(e){
        if (e.key === 'Enter') {
          let count = document.getElementById('guess-content').children.length + 1;
          guesstxt = $(guess).val();
          if (guesstxt == 'test') {
            guess_copyandpaste = guess_copyandpaste + 'GUESS ' + String(count) + ': CORRECT! 😁' + '\n'
            onOutcome()
          }
          else {
            guess_copyandpaste = guess_copyandpaste + 'GUESS ' + String(count) + ': INCORRECT 😭' + '\n'
          }
          $('#guess-content').append("<p class = 'guess'>" + 'GUESS ' + String(count) + ': ' + guesstxt + "</p>")
          $(guess).val('')
        }
        
      })

      const button = document.getElementById('share-button')

      var outcome_div = document.getElementById('outcome');
      var outcome_txt = document.getElementById('outcome-text');

      // Little code block to stop the div from disappearing when clicking in the text - will disappear when clicking outside.
      outcome_div.addEventListener("click", function () {
        $('#outcome').fadeOut(100);
      }, false);
      outcome_txt.addEventListener("click", function (ev) {
          console.log('Does this work?');
          ev.stopPropagation();
      }, false);

      button.addEventListener('click', function(){
        document.getElementById("share-button").innerHTML = "Copied to Clipboard!";
        navigator.clipboard.writeText(guess_copyandpaste)
      })

});

// Overlay for the rules - turns the rules on and off

function onRules() {
    document.getElementById("overlay").className = 'fade-in';
    document.getElementById("overlay").style.display = "block";
  }

// Same principle here - for the share page

function onShare() {
    document.getElementById("share").className = 'fade-in';
    document.getElementById("share").style.display = "block";
  }

function onThanks() {
    document.getElementById("thanks").className = 'fade-in';
    document.getElementById("thanks").style.display = "block";
}

function onOutcome() {
  document.getElementById("outcome").className = 'fade-in';
  document.getElementById("outcome").style.display = "block";
}