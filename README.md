# ednevnik_scraper

## install
gcal - `pip3 install --upgrade google-api-python-client oauth2client`  
bs4 - `pip3 install beautifulsoup4`  

## config
### scraper
add your username and password to `cred.py`

### google calendar
- go to https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the
  click on the button `ENABLE THE GOOGLE CALENDAR API`, create a project (or use existing on), download credentials.json and move them to the root of repo
- change `calendarId` on line 32 in `gcal_test.py`

## run
just scraping (returns json)  
`python3 login_test.py`  

import to gcal  
`python3 gcal_test.py`  
