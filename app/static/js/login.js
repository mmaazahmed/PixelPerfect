// Creating the collapsible sidebar for guesses

$(window).on('load', () => {
  

  // Initialising required constants
  const overlay_div = document.getElementById('overlay')
  const overlay_txt = document.getElementById('overlay-text')

  const share_div = document.getElementById('share')
  const share_txt = document.getElementById('share-text')

  const thanks_div = document.getElementById('thanks')
  const thanks_txt = document.getElementById('thanks-text')

  const button = document.getElementById('share-button')
  const web_button = document.getElementById('share-website')

  const themes_div = document.getElementById('themes');
  const themes_txt = document.getElementById('themes-text');

  const stats_div = document.getElementById('stats');
  const stats_txt = document.getElementById('stats-text');

  const leaderboard_div = document.getElementById('leaderboard');
  const leaderboard_txt = document.getElementById('leaderboard-text');

  const base_theme = document.getElementById('base-theme')
  const light_theme = document.getElementById('light-theme')
  const cameron_theme = document.getElementById('cameron-theme')
  const maaz_theme = document.getElementById('maaz-theme')

  // Code blocks to stop the div from disappearing when clicking in the text field, but to disappear when clicking outside the field.
  share_div.addEventListener("click", function() {
    $('#share').fadeOut(100);
  }, false);
  share_txt.addEventListener("click", function(ev) {
    ev.stopPropagation();
  }, false);

  $(overlay_div).click(function() {
    $('#overlay').fadeOut(100)
  })
  overlay_txt.addEventListener("click", function(ev) {
    ev.stopPropagation();
  }, false);

  $(thanks_div).click(function() {
    $('#thanks').fadeOut(100)
  })
  thanks_txt.addEventListener("click", function(ev) {
    ev.stopPropagation();
  }, false);

  themes_div.addEventListener("click", function() {
    $('#themes').fadeOut(100);
  }, false);

  themes_txt.addEventListener("click", function(ev) {
    ev.stopPropagation();
  }, false);

  stats_div.addEventListener("click", function() {
    $('#stats').fadeOut(100);
  }, false);

  stats_txt.addEventListener("click", function(ev) {
    ev.stopPropagation();
  }, false);

  leaderboard_div.addEventListener("click", function() {
    $('#leaderboard').fadeOut(100);
  }, false);

  leaderboard_txt.addEventListener("click", function(ev) {
    ev.stopPropagation();
  }, false);

  const current_theme = document.getElementById('background');
  const share_infotxt = document.getElementById('share-infotxt')
  const rules_infotxt = document.getElementById('rules-infotxt')
  const thanks_infotxt = document.getElementById('thanks-infotxt')

  base_theme.addEventListener('click', function() {
    current_theme.className = base_theme.id;
    base_theme.innerHTML = 'Base Theme: Selected!';
    light_theme.innerHTML = 'Light Theme';
    maaz_theme.innerHTML = 'Maaz Theme';
    cameron_theme.innerHTML = 'Cameron Theme';
    $('#main-title').css('color', 'white');
    $("li").hover(function(){
      $(this).css('transition', 'background 0.1s');
      $(this).css("background", "rgb(39,39,39)");
      $(this).css("border-radius", "10px");
      }, function(){
      $(this).css("background", "rgb(39,39,39)");
      });
    thanks_txt.className = 'base';
    overlay_txt.className = 'base';
    leaderboard_txt.className = 'base';
    stats_txt.className = 'base';
    themes_txt.className = 'base';
    share_txt.className = 'base';
    share_infotxt.className = 'info-text-base'
    rules_infotxt.className = 'info-text-base'
    thanks_infotxt.className = 'info-text-base'
    
  });

  light_theme.addEventListener('click', function() {
    current_theme.className = light_theme.id;
    base_theme.innerHTML = 'Base Theme';
    light_theme.innerHTML = 'Light Theme: Selected!';
    maaz_theme.innerHTML = 'Maaz Theme';
    cameron_theme.innerHTML = 'Cameron Theme';
    $('#main-title').css('color', 'grey');
    $("li").hover(function(){
    $(this).css('transition', 'background 0.1s');
    $(this).css("background", "rgb(200,200,200)");
    $(this).css("border-radius", "10px");
    }, function(){
    $(this).css("background", "rgb(39,39,39)");
    });
    thanks_txt.className = 'light';
    overlay_txt.className = 'light';
    leaderboard_txt.className = 'light';
    stats_txt.className = 'light';
    themes_txt.className = 'light';
    share_txt.className = 'light';
    share_infotxt.className = 'info-text-light'
    rules_infotxt.className = 'info-text-light'
    thanks_infotxt.className = 'info-text-light'
  });

  maaz_theme.addEventListener('click', function() {
    current_theme.className = maaz_theme.id;
    base_theme.innerHTML = 'Base Theme';
    light_theme.innerHTML = 'Light Theme';
    maaz_theme.innerHTML = 'Maaz Theme: Selected!';
    cameron_theme.innerHTML = 'Cameron Theme';
    $('#main-title').css('color', 'white');
    $("li").hover(function(){
      $(this).css('transition', 'background 0.1s');
      $(this).css("background", "rgb(1,130,40)");
      $(this).css("border-radius", "10px");
      }, function(){
      $(this).css("background", "rgb(39,39,39)");
      });
    thanks_txt.className = 'maaz';
    overlay_txt.className = 'maaz';
    leaderboard_txt.className = 'maaz';
    stats_txt.className = 'maaz';
    themes_txt.className = 'maaz';
    share_txt.className = 'maaz';
    share_infotxt.className = 'info-text-maaz'
    rules_infotxt.className = 'info-text-maaz'
    thanks_infotxt.className = 'info-text-maaz'

  });

  cameron_theme.addEventListener('click', function() {
    current_theme.className = cameron_theme.id;
    base_theme.innerHTML = 'Base Theme';
    light_theme.innerHTML = 'Light Theme';
    maaz_theme.innerHTML = 'Maaz Theme';
    cameron_theme.innerHTML = 'Cameron Theme: Selected!';
    $('#main-title').css('color', 'white');
    $("li").hover(function(){
      $(this).css('transition', 'background 0.1s')
      $(this).css("background", "linear-gradient(47deg, rgba(238,0,255,1) 0%, rgba(126,0,255,1) 100%)");
      $(this).css("border-radius", "10px");
      }, function(){
      $(this).css("background", "rgb(39,39,39)");
      });
    thanks_txt.className = 'cameron';
    overlay_txt.className = 'cameron';
    leaderboard_txt.className = 'cameron';
    stats_txt.className = 'cameron';
    themes_txt.className = 'cameron';
    share_txt.className = 'cameron';
    share_infotxt.className = 'info-text-cameron'
    rules_infotxt.className = 'info-text-cameron'
    thanks_infotxt.className = 'info-text-cameron'
  });




  // When the share button is clicked, copy the share text to clipboard.
  button.addEventListener('click', function() {
    document.getElementById("share-button").innerHTML = "Copied to Clipboard!";
    navigator.clipboard.writeText(guess_copyandpaste)
  });

  web_button.addEventListener('click', function() {
    web_button.innerHTML = 'Copied to Clipboard!';
    navigator.clipboard.writeText(window.location.href);
  });

  $('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
 });

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

function onThemes() {
  document.getElementById("themes").className = 'fade-in';
  document.getElementById("themes").style.display = "block";
};

function onStats() {
  document.getElementById("stats").className = 'fade-in';
  document.getElementById("stats").style.display = "block";
};

function onLeaderboard() {
  document.getElementById("leaderboard").className = 'fade-in';
  document.getElementById("leaderboard").style.display = "block";
};


