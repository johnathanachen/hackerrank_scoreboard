import re
import requests
import bs4 as bs
import urllib

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

# start session
session = requests.Session()

login_url = "https://www.hackerrank.com/login?h_r=community_home&h_v=log_in&h_l=header_right"
r = session.get(login_url)
soup = bs.BeautifulSoup(r.text)

login_input = soup.find('input', {'id':'login'})

for tr in trs:
    span = tr.find('span')
    cle = span.get('id')

    url = 'https://j2c-com.com/Euronaval14/catalogueWeb/ajaxSociete.php?cle=' + cle + '&rnd=' + generate_random_number(0,9999999999999999)
    pop = session.post(url)  # <-- the POST request here contains cookies returned by the first GET call

    print url
    print pop.text

    break

def connect_site():
    site_url = 'https://www.hackerrank.com/'
    site_url_request = requests.get(site_url, headers=headers)
    site_url_request.raise_for_status()
    soup_final = bs.BeautifulSoup(site_url_request.text, 'lxml')

    print(soup_final)

connect_site()

