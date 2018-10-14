# ednevnik_scraper

## Licence
Like really ? OPEN SOURCE  
use it however you want to, if you build something cool let me know (PR or Issue)  
Happy hacking 👨‍💻

## Install
- `pip3 install --upgrade google-api-python-client oauth2client`  
- `pip3 install beautifulsoup4`  

## Config
### scraper
- add your username and password to `cred.py`

### google calendar
- Go to https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the, click on the button `ENABLE THE GOOGLE CALENDAR API`, create a project (or use existing on), download credentials.json and move them to the root of repo
- change `calendarId` on line 32 in `gcal_test.py`

## Run
Just scraping (returns json)  
`python3 login_test.py`  

Import to gcal  
`python3 gcal_test.py`  
