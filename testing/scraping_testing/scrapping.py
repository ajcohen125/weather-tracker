#import packages for urls
from urllib.request import urlopen, Request
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


#Set url and open page
#url = "https://roberteads.github.io"

url = str(sys.argv[1]) #Allows URL to be passed throught from runtime

#Helps reading the page
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'} 
req = Request(url=url, headers=headers)
page = urlopen(req)

#Read the page
html_bytes = page.read()
html = html_bytes.decode("utf-8")

#writing the raw html data to a file
write_file = open("raw_html.htm", "w")
write_file.write(html)
write_file.close()

#Feeding raw html through parser to determine data
parser = MyHTMLParser()
parser.feed(html)

