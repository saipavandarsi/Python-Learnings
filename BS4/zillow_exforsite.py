from bs4 import BeautifulSoup as BS
import time
import requests

def get_soup(s):
    try:
        return BS(s)
    except Exception, e:
        return none

out = open("resultfromzillow.csv",'w+')
s = """
https://www.zillow.com/homes/cleaveland_rb/
"""

r = requests.get(s)
soup = get_soup(r.text)

if soup:
    divs = soup.findAll('div', {'class':'main-wrapper '})
    if divs:
        for i in divs:
            try:
                container = i.find('header',{'zss-header pinnable-header zsg-layout-width layout-width_marginless'}).text
                #out.write(container)
                out.write(container.encode('ascii','ignore'))
                #We can automate after tge
            except Exception, e:
                print 'Exception Occured'

out.close()