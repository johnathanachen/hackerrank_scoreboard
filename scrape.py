import requests
import re
import bs4 as bs
from lxml import html

USERNAME = "jcswift7@gmail.com"
PASSWORD = "TYurKpN2ztsv"

LOGIN_URL = "https://www.hackerrank.com/login"
URL = "https://www.hackerrank.com/leaderboard?friends=follows&page=1&practice=algorithms"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        # "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    soup_final = bs.BeautifulSoup(result.text, 'lxml')

    # List of leaderboard names
    hacker_name = [item["data-value"] for item in soup_final.find_all() if "data-value" in item.attrs]
    hacker_points = [item["data-attr10"] for item in soup_final.find_all() if "data-attr10" in item.attrs]
    print(hacker_name)
    print(hacker_points)

if __name__ == '__main__':
    main()
