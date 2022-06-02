# CITS3403-Project

## CITS3403 Project: Pixel Perfect

### By Sean Ledesma, Mohammed Maaz Ahmed, Pablo Nayendov, and Cameron Roth.

#### Individual Roles:

Sean: Database management and implementation

Maaz: Server implementation and database reworking

Pablo: Keyboard JS, Statistics Implementation

Cameron: Front-end HTML, CSS, JS

## How to run:
run  pip install -r /path/to/requirements.txt to installl packages/modules
activate virtual environment and run the command flask run to run the app.

## App structure:
images/daily puzzles are stored in ./app/static/images/images directory  
  
names of each image is stored in the database along with its deploy date, pixelfactors,and answer to the puzzle  
  
Pixelated versions of the daily image will be name 1.png,2.png ... 5.png with 1 being the most pixelated and 5 being the least.  
On start up the __init__.py will create 3 folders with yesterday's,today's and tomorrows date through the PixelPerfectinitilization() function  
It will then pull the image names from the database corresponding to these dates. Dates are formated in the following order month-day-year with leading zeros.  
it will then create 5 versions of each image with varying degrees of the pixelation and store them to the folder corresponding to their date.  
Pixelfactors are 5 digits are stored as a string and separeated by a '/' in the database. Each digit indicates the degree of pixelation of the image.  
JS in the front formats the date client side to match the format in the database, appends it to the image path, and alters the img src in the HTML to display  
each image. The image number is incremented with each guess.  
After every 25 hours, the create_new_puzzle() function will  be called, which will remove the folder with the date two days from now, and will create another folder
with tomorrows date and will populate it with the daily image corresponding to tommorrow's date.  

The decision to render the pixelated images server side rather than client side was made due to the inefficiency of the pixelation algorithm, and rather than having it be pixelated on the fly for each user everytime on loading, it was decided to render each image once for every user.  
