#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys

username = ""
password = ""

url = "https://baconbits.org/login.php"

def main():
    session = requests.session()
    # session = requests.session(config={'verbose':sys.stderr}) For being verbose
    login_data = {'username': username, 'password':password, 'submit':'Log In!'}

    r = session.post(url, data=login_data)

    r = session.get('https://baconbits.org/user.php?id=10084')
    body = r.content
    soup = BeautifulSoup(body)
    # This will print out the userinfo_stats section that contains the data.
    # print soup.find('ul', id='userinfo_stats')
    # Works bitch !
    userstats = soup.find_all('span', class_="stat")
    print 'Name: user/name/here'
    print 'Upload:', userstats[0].text
    print 'Download:', userstats[1].text
    print 'Ratio:', userstats[2].text

if __name__ == '__main__':
    main()
