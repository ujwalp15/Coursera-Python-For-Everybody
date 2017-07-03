import urllib
from BeautifulSoup import *
import ssl
import re

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
depth = 8
initial_url = 'http://python-data.dr-chuck.net/known_by_Marisa.html'

def follow_url(url, depth):
    if depth > 0:
        get_name(url)
        soup = BeautifulSoup(urllib.urlopen(url, context=scontext).read())
        follow_url(soup('a')[17].get('href', None), depth - 1)

def get_name(url):
    print re.findall('known_by_([A-Z][a-z]+).html', url)[0],

follow_url(initial_url, depth)
