import urllib
headjack = urllib.urlopen("http://data.pr4e.org/intro-short.txt")

for line in headjack:
    print(line.strip())

print(headjack.info())
