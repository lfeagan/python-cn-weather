import requests
from BeautifulSoup import BeautifulSoup
from itertools import islice

r = requests.get('http://www.nmc.cn/publish/forecast/ASH/shanghai.html')
#print(r.status_code)
#print('content-type: ' + r.headers['content-type'])
#print('encoding: ' + r.encoding)
#print(r.text)
soup = BeautifulSoup(r.text)
day0 = soup.find("div", {"id": "day0"})
xdsd = day0.find("div", {"class": "row xdsd"})
for i in islice(xdsd,2,None):
  print i.string
quit()
