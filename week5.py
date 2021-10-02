import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

address = input('Enter location: ')
data = urllib.request.urlopen(address).read()
tree = ET.fromstring(data)
sum = 0
for x in tree.findall('.//comment'):
    y = x.find('.//count').text
    sum = sum + int(y)
print(sum)
