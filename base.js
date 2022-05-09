$(window).on('load', () => { 
    var coll = document.getElementsByClassName("collapsible");
      console.log(coll)
      var i;
      
      for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
          console.log('is this even working')
          this.classList.toggle("active");
          var content = this.nextElementSibling;
          if (content.style.maxHeight){
            content.style.maxHeight = null;
          } else {
            content.style.maxHeight = content.scrollHeight + "px";
          } 
        });
      }
});

function onRules() {
    document.getElementById("overlay").style.display = "block";
  }
  
function offRules() {
    document.getElementById("overlay").style.display = "none";
  }

function onShare() {
    document.getElementById("share").style.display = "block";
  }

function offShare() {
    document.getElementById("share").style.display = "none";
  }
