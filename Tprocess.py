from multiprocessing import Process
import os
import time
import requests
from bs4 import BeautifulSoup

start = time.time()
print("start processing")

urls = [
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
]


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


def calc(cor=None, url=None):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
        st=time.time()
        emails = ''
        res = requests.get(url, headers=headers)
        content = BeautifulSoup(res.text, 'html.parser')
        emails = classbase_email(content)
    
        print('url {} \n\n emails {}\n\n'.format(url, emails))
        print('time {} \n\n'.format(time.time() - st))     

processes = []

for i in range(os.cpu_count()):
	print('registering process %d' % i)
	processes.append(Process(target=calc(i, urls[i])))

for process in processes:
	process.start()

for process in processes:
	process.join()
 
end = time.time()

print(end - start)