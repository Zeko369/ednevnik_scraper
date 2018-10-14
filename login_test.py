import requests
from lxml import html
from bs4 import BeautifulSoup
from cred import credentials

class scraper(credentials):
  def __init__(self):
    super().__init__()
    self.LOGIN_URL = "https://ocjene.skole.hr/pocetna/posalji/"
    self.URL = "https://ocjene.skole.hr/pregled/ispiti/2193825230"

  def scrape(self):
    self.get_page()
    self.get_data()

  def get_page(self):
    session_requests = requests.session()

    # Get login csrf token
    self.result = session_requests.get(self.LOGIN_URL)
    tree = html.fromstring(self.result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]

    # Create payload
    payload = {
        "user_login": self.username, 
        "user_password": self.password, 
        "csrf_token": authenticity_token
    }

    # Perform login
    self.result = session_requests.post(self.LOGIN_URL, data = payload, headers = dict(referer = self.LOGIN_URL))
    # Scrape url
    self.result = session_requests.get(self.URL, headers = dict(referer = self.URL))

  def get_data(self):
    data = self.result.text
    soup = BeautifulSoup(data, features="lxml")

    self.out = []

    for link in soup.find_all('tr'):
      test = dict()
      i = 0
      for child in link.children:
        if(len(child.string) > 1):
          if i == 0:
            test['subject'] = child.string
          elif i == 1:
            test['name'] = child.string
          elif i == 2:
            if child.string == 'Datum':
              test['error'] = True
              continue
            test['date'] = child.string
          else:
            test['error'] = True
          i += 1
      if(len(test.keys()) == 3 and 'error' not in test.keys()):
        self.out.append(test)

if __name__ == '__main__':
  scrape = scraper()
  scrape.scrape()
  print(scrape.out)