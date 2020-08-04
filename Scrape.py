import requests
from bs4 import BeautifulSoup
r = requests.get('https://aws.amazon.com/blogs/aws/')
soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('a'):
 if 'category' in str(link):
  print(link.get('href'))
