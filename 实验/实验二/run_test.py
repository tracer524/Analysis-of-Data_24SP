from urllib.request import urlopen
import re 

response = urlopen(url="https://dblp.dagstuhl.de/pid/211/5760.html")
html = response.read().decode("utf-8")
html.split()
