from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import requests
import re

start = time.time()
print("request process")

def email_scraper(content):
    reg = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    emails = set([email for email in re.findall(reg, str(content))])
    
    if content.select('.__cf_email__') != []:
        emails.update(classbase_email(content))
    
    return emails


def classbase_email(content):
    emails = set()
    
    try:
        for link in content.select('.__cf_email__'):
            email = link.get('data-cfemail')
            emails.add(email) 
    except Exception as e:
        print('classbase email error', e)

    emails = email_decoder(emails)
    
    return emails


def email_decoder(emails=None):
    email_lists = set()

    for email in emails:
        try:
            r = int(email[:2],16)
            email = ''.join([chr(int(email[i:i+2], 16) ^ r) for i in range(2, len(email), 2)])
            email_lists.add(email) 
            
        except Exception as e:
            print('email decoder error ', e) 
            
    return email_lists


url = "https://www.azacp.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
emails = email_scraper(soup)
print('emails', emails)

end = time.time()

print(end - start)