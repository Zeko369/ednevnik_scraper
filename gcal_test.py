from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

from login_test import scraper

class google_calendar_ednevnik_thingy:
  def __init__(self):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    self.service = build('calendar', 'v3', http=creds.authorize(Http()))

    self.scraper = scraper()
    self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return

  def run(self):
    self.scraper.scrape()

    for test in self.scraper.out:
      print('Inserting: ', test)
      self.create_event(self.event(test))

  def create_event(self, event):
    self.service.events().insert(calendarId='eeclo4qf24cgae8jtaph7mojc8@group.calendar.google.com', body=event).execute()
    return

  def parse_name(self, subject, name):
    return subject + ' - ' + name

  def parse_data(self, date, end):
    date = date.split('.')[:-1]
    day, month, year = int(date[0]), int(date[1]), int(date[2])
    if(end):
      day += 1

    if day > self.month_days[month - 1]:
      day = 1
      month += 1
      if month == 13:
        year += 1
        month = 1    

    return datetime.date(year, month, day).isoformat()

  def event(self, data):
    return {
      'summary': self.parse_name(data['subject'], data['name']),
      'start': {
        'date': self.parse_data(data['date'], 0),
        'timeZone': 'Europe/Zagreb',
      },
      'end': {
        'date': self.parse_data(data['date'], 1),
        'timeZone': 'Europe/Zagreb',
      }
    }

if __name__ == '__main__':
  main = google_calendar_ednevnik_thingy()
  main.run()

# print ('Event created: %s' % (event.get('htmlLink')))
