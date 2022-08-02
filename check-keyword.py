# function that check if a word is included on a website
from ast import keyword

from pyparsing import Keyword


def check_keyword(url, keyword):
    """
    function that check if a word is included on a website
    """
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url) # get the html code of the website
    soup = BeautifulSoup(r.text, "html.parser") # parse the html code
    if keyword in soup.text: # check if the word is included on the website
        print("The keyword is on the page")
        print(keyword)
    else: # if the word is not included on the website
        print("The keyword is not on the page")

url = 'http://www.insert-url-here.com'
keyword = 'keyword-to-check'

# function that call on a function every 15 minutes
def check_keyword_every_5_seconds(url, keyword):
    import time
    while True:
        check_keyword(url, keyword)
        time.sleep(15*60) # wait 15 minutes


check_keyword_every_5_seconds(url, keyword)