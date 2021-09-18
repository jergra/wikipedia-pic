September 16, 2021

acer travelmate
C:\webdev\pictureProj2>

this is a flask website which is a stand-alone display of the 
wikipedia 'today's featured picture' which is down the 
wikipedia main page:
    https://en.wikipedia.org/wiki/Main_Page
wikipedia has its own stand-alone display:
    https://en.wikipedia.org/wiki/Template:POTD_protected

the inspiration for this project is from exploring the 
wikipedia API, the main page of which is:
    https://www.mediawiki.org/wiki/API:Main_page

there, I found a tutorial with python and flask code to 
build a 'Picture of the day viewer'. Since this only
retrieved the picture and not the caption, I took another
approach and found scraping code which I used to 
scrape wikipedia's stand-alone page. The caption's
html code was removed using BeautifulSoup.

The only advantage of this project over wikipedia's page is that 
the picture is larger. The disadvantage is that, because of the 
BeautifulSoup, links within the caption are gone.


to activate the virtual environment, type:
    ./my_venv/Scripts/activate

start locally:
    python app.py

deployed at:
    https://wikipedia-pic.herokuapp.
    
to update:
    activate virtual environment: ./my_venv/Scripts/activate
    git add .
    git commit -m "message"
    git push
    go to heroku dashboard, select wikipedia-pic, under 'Deploy',
        bottom of page, click 'Deploy Branch'

