#!/usr/bin/env python

import requests
import sys
from bs4 import BeautifulSoup

# Atom feed for GMail
url = "https://mail.google.com/mail/feed/atom"

# username and password

username = ""
password = ""

def get_unread_count():
    session = requests.session()
    r = requests.get(url, auth=(username, password))
    content = r.text
    soup = BeautifulSoup(content, "xml")
    count = soup.feed.fullcount.contents[0]
    return count.encode()


def main():
    print "Unread Email: %s" % get_unread_count()


if __name__ == '__main__':
    main()
