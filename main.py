from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('credentials.json')
#  creds = store.get()
#  if not creds or creds.invalid:
flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

pph = 25

# Call the Calendar API
now = datetime.datetime.now() - datetime.timedelta(days=10)
now = datetime.date(2018, 6, 15)
now = now.isoformat() + 'T00:00:00.545779Z'
#  now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print(now)
events_result = service.events().list(calendarId='k6cqrr6fvguk29phfqkfonigms@group.calendar.google.com', timeMin=now,
                                      maxResults=1000, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

def length(event):
    a = event['start']['dateTime'][11:][:-6].split(':')
    b = event['end']['dateTime'][11:][:-6].split(':')

    x = 0
    y = 0

    x = int(b[0]) - int(a[0])
    y = int(b[1]) - int(a[1])

    if(x < 0):
        x = 0
        y = 60 + x
    if(y < 0):
        x -= 1
        y = 60 + y

    return x * 60 + y

tmp = 0

if not events:
    print('No upcoming events found.')
for event in events:
    #  print(event['summary'], length(event) * (pph / 60))
    tmp += length(event)
    if(event['summary'] == '!!!isplata'):
        tmp = 0

tmp *= (pph / 60)
print(tmp)
