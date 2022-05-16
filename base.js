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

      const ruleoverlay = document.getElementById('overlay')
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

      guess.addEventListener("keypress", function(e){
        if (e.key === 'Enter') {
          let count = document.getElementById('guess-content').children.length + 1;
          guesstxt = $(guess).val();
          $('#guess-content').append("<p class = 'guess'>" + 'GUESS ' + String(count) + ': ' + guesstxt + "</p>")
          $(guess).val('')
        }
        
      })

});

// Overlay for the rules - turns the rules on and off

function onRules() {
    document.getElementById("overlay").className = 'fade-in';
    document.getElementById("overlay").style.display = "block";
  }
  
function offRules() {
    document.getElementById("overlay").className = 'fade-out';
    // document.getElementById("overlay").style.display = "none";
  }

// Same principle here - for the share page

function onShare() {
    document.getElementById("share").className = 'fade-in';
    document.getElementById("share").style.display = "block";
  }

function offShare() {
    document.getElementById("share").className = 'fade-out';
    // document.getElementById("share").style.display = "none";
  }

function onThanks() {
    document.getElementById("thanks").className = 'fade-in';
    document.getElementById("thanks").style.display = "block";
}

function offThanks() {
    document.getElementById("thanks").className = 'fade-out';
    // document.getElementById("share").style.display = "none";
}