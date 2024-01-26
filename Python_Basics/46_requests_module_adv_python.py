import requests, os
from bs4 import BeautifulSoup

os.chdir('Python\\Python_Basics')

url1 = 'https://animedaily.net/full-level-rich-daughter-makes-a-strong-comeback-novel.html'
response = requests.get(url1, timeout=3)
print(response.ok)
print(response.status_code)
'''
status codes so anything within range
>=200 and <300 ---> good response
>=300 and <400 ---> Redirection
>=400 and <500 ---> Client side error
>=500 ----> Client side error 
'''
print(response.raise_for_status())
# print(response.text)
# print(response.headers)
print(response.headers['content-type'])

image_url = 'https://static.bunnycdn.ru/i/cache/images/b/ba/bad455c952ee9bfe757782077baf4114.jpg'

response = requests.get(image_url).content # this enable to get the content in hexdecimal format, which we can save
with open('image.png','wb') as img:
    img.write(response)


some_dict = {'v':'jS4aFq5-91M'}
url_2 = 'https://www.youtube.com/'
response = requests.get(url_2,params=some_dict)
print(response.url, response.status_code)

'''
Notes on http methods
get = read data
post = create data
put = update data
delete = delete data

similar to CRUD  - Create, Retrieve/Read, Update, Delete
'''