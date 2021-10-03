"""
    app.py
    MediaWiki API Demos

    Fetches Wikipedia Picture of the Day (POTD) and displays it on a webpage.
    Also allows users to go backward or forward a date to view other POTD.

    MIT License
"""
from datetime import date, timedelta, datetime
from flask import Flask, render_template, request
import requests


APP = Flask(__name__)
SESSION = requests.Session()
ENDPOINT = "https://en.wikipedia.org/w/api.php"

CURRENT_DATETIME3 = datetime.today() + timedelta(hours=0)
print("CURRENT_DATETIME3:", CURRENT_DATETIME3)
CURRENT_DATE3 = date.today() + timedelta(hours=0)
print("CURRENT_DATE3:", CURRENT_DATE3)
print("CURRENT_DATETIME3.date():", CURRENT_DATETIME3.date())

CURRENT_DATE = CURRENT_DATETIME3.date()
print("CURRENT_DATE:", CURRENT_DATE)

@APP.route("/", methods=["GET", "POST"])
def index():
    """
    Requests data from Action API via 'fetch_potd' function & renders it on the
    index page accessible at '/'
    """

    if request.method == "POST":
        change_date()

    data = fetch_potd(CURRENT_DATE)

    return render_template("index.html", data=data)


def change_date():
    """
    Changes current date in response to input from the web form
    """

    global CURRENT_DATE

    user_input = request.form["change_date"]
    new_date = CURRENT_DATE
    last_date = date.today()
    first_date = date(year=2004, month=5, day=14)

    if user_input == "← Back":
        new_date = new_date - timedelta(days=1)
    elif user_input == "Next →":
        new_date = new_date + timedelta(days=1)

    if new_date > last_date or new_date < first_date:
        return

    CURRENT_DATE = new_date


def fetch_potd(cur_date):




    date_iso = cur_date.isoformat()
    title = "Template:POTD protected/" + date_iso
    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": title
    }
    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()
    filename = data["query"]["pages"][0]["images"][0]["title"]
    



    cur_dateString = str(cur_date)
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": "Template:POTD_protected/" + cur_dateString,
        "format": "json"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    theData = DATA["parse"]["text"]["*"]
    print("THE_DATA:", theData)
    a = theData.find('0">\n<p>')
    b = theData.find('<p style="text-align:')
    print("a:", a)
    print("b:", b)
    c = theData[a + 3:b]
    print("------------------------------")
    print("THE_DATA from a to b:")
    print(c)
    c = c.replace('href="', 'href="https://en.wikipedia.org')
    print("------------------------------")
    print(c)
    print("------------------------------")
    
    g = theData.find('1.5x, //upload')
    h = theData.find(' 2x" data')
    print("g:", g)
    print("h:", h)
    i = theData[g + 8:h]
    print("THE_DATA from g to h:", i)
    print("IMAGE_SRC:", 'https://' + i)
    
    j = theData.find('href="/wiki/File:')
    k = theData.find(' class="image" title')
    print("j:", j)
    print("k:", k)
    m = theData[j + 17:k - 5]
    print("THE_DATA from j to k:", m)
    
    print("FILENAME1:", m)
    print("FILENAME2:", filename)
    croppedFilename = filename[5:-4]
    print("croppedFILENAME2:", croppedFilename)

    image_data = {
        # "filename": m,
        "filename": croppedFilename,
        "image_src": 'https://' + i,
        "image_page_url": 'https://en.wikipedia.org/wiki/Template:POTD_protected/' + cur_dateString,
        "date": cur_date,
        "caption": c
    }

    return image_data

""" Commment these two lines for deployment in Toolforge """
if __name__ == "__main__":
    APP.run()

