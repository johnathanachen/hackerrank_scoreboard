import requests
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
    tree = html.fromstring(result.content)
    hackername = tree.xpath("<div class='inline-block middle hacker-name text-ellipsis'>ajboxjr</div>")

    print(hackername)

if __name__ == '__main__':
    main()