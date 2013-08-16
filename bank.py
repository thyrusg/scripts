import requests
from bs4 import BeautifulSoup

# To-Do: Allow user to specifiy the number of transaction they want

# RSS Feed of Bank Transaction
url = ""

def parse_transaction(feed):
    # Will parse the returned transactions and print them in a nice format
    """
    This is how the information should appear once it's printed:
    
    Date            Action          Amount
    6-24-2013       Withdrawal      56.00	

    There are 3 tabs between each category
    """
    
    # Loop through all of the transactions
    for transaction in feed:
        print transaction
    # this will print all of the transact

    for transaction in feed.find_all(["title", "pubDate"]):
       format_transaction(transaction)
       format_date(transaction)
    # This will print the following
    # <title>$69.00 | ATM Deposit #000614 | 38 days ago</title>
    # <pubDate>Fri, 17 May 2013 00:00:00 GMT</pubDate>


def format_transaction(transaction):
    # This function will take a transaction:

    # <title>$69.00 | ATM Deposit #000614 | 38 days ago</title>

    # And format it as follows:

    """
    This is how the information should appear once it's printed:
          
     Date            Action          Amount
     6-24-2013       Withdrawal      56.00   
      
     There are 3 tabs between each category
     """
    amount = int
    transType = str

    actionList = ["Deposit", "Withdrawl"]
    # Convert to string
    str(transaction)
    # Splite the string at the | 
    transAction = transaction.split("|")
    amount = transAction[0]
    if "Deposit" in actionList:
        transType = "Deposit"
    else:
        transType = "Withdrawl"
    return (amount, transType)
    


def format_date(aDate):
    # This function will take a date in the following format:

    # <pubDate>Fri, 17 May 2013 00:00:00 GMT</pubDate
    # Then return it as Month-Date-Year so, 6-24-2013

    dateAbbrev = {"Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thu":"Thursday", "Friday":"Friday"}

    for date in dateAbbrev.
    
    pass


def connect_to_bank(url):
    # Setuo a session so we don't have to constantly reauthenticate
    session = requests.session()
    
    # Establish the connection
    r = requests.get(url)

    # Check if the connection was successful 
    if r.status_code != 200:
        print "Could Not Access Feed"
    else:
        pass

    return r.text

def main():
    parse_transaction(connect_to_bank(url))
    
if __name__ == '__main__':
    main() 
