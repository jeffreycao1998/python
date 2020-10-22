from urllib.request import urlopen
html = urlopen('https://www.google.ca/')
print(html.read())