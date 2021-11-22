from multiprocessing import Process
import os
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import concurrent.futures


process_time = 0
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
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
    'https://chesterplumber.co.uk',
    'https://www.accesswire.com/contact',
    'https://www.3dnamewallpapers.com/contact',
    'https://www.plumbers-maidstone.co.uk/',
    'https://www.ukplumbingcontractors.com/contact',
    'https://chesterplumber.co.uk/contact-us/',
    'https://www.wsplumbing.co.uk/contacts/',
    'https://www.raulfs-sanitaer.de/',
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


def calc(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
        dd = datetime.utcnow()
        print('start ',dd)
        emails = ''
        st=time.time()
        # rt=time.time()
        res = requests.get(url, headers=headers)
        # print('take request time {} \n\n'.format(time.time() - rt))     
        
        pt=time.time()
        content = BeautifulSoup(res.text, 'html.parser')
        # Process(target=classbase_email(content))
        p1 = Process(target = classbase_email, args =(content, ))
        p1.start()
        p1.join()
        # emails = classbase_email(content)
        prot = time.time() - pt
        global process_time
        process_time += prot
        print('\n\ntake process time {} \n\n'.format(prot))     
        
        print('\n\n')
        # print('url {} \n\n emails {}\n\n'.format(url, emails))
        # print('\n\ntime {} \n\n'.format(time.time() - st))      

MAX_THREAD = 8
def main():
    threads = min(MAX_THREAD, len(urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(calc, urls)


main()
# main()
# main()
# main()
end = time.time()

print('total urls {}'.format(len(urls)))
print('total process time {}'.format(process_time))
print('Average process time {}'.format(process_time/len(urls)))
print(end - start)