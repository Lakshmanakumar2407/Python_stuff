from bs4 import BeautifulSoup
import requests, os, csv

# changing Directory
os.chdir(r'Python\Python_Basics\Web_scrapping')

# Creating a html file to store the content from requests
html_file = open('01_html_code.html','w', encoding='utf-8')

# using requests get method to get source object
source = requests.get('https://www.scrapethissite.com/pages/simple/')
html_file.write(source.text) # write the text to html file using the text attribute of source object
html_file.close()

html_file = open('01_html_code.html')

# Parsing the html file using beautifulsoup
soup = BeautifulSoup(html_file, 'lxml')

i = 0
# creating a dict to store scrapped values
scrap_dict = {}

# creating a function to remove unwanted spaces in the scrapped country name
def removal(some_string):
    t = some_string.lstrip('\n\n                            ')
    t =t.rstrip('\n                       ')
    return t

# parsing...
for article in soup.find_all('div', class_ = 'row'):
    # ignoring first three rows and last 2 cols, can use try except for the i>86 part
    if i<3 or i>86:
        trash = article
    else:
        for row_article in article.find_all('div', class_= 'col-md-4 country'):
            country_name = row_article.h3.text
            country_info  = row_article.find('div', class_='country-info')
            country_capital = country_info.find('span', class_ ='country-capital').text
            country_poulation = country_info.find('span', class_ ='country-population').text
            country_area = country_info.find('span', class_ ='country-area').text
            scrap_dict[removal(country_name)] = [country_capital, country_poulation ,country_area]
    i+=1

# sorting the dict based on country names...
scrap_dict = dict(sorted(scrap_dict.items()))

# creating a csv to store the scraped data
with open('01_scrapped_csv_country_list.csv', 'w', newline= '') as scrap_csv:
    header = ['country','capital','population','area']
    scrap_csv = csv.DictWriter(scrap_csv, fieldnames=header, delimiter=',')
    scrap_csv.writeheader()
    for key in scrap_dict.keys():
        # shows Dictwriter not subscritable erro so had to do this...
        country_i, capital_i, population_i, area_i = key, scrap_dict[key][0], scrap_dict[key][1], scrap_dict[key][2]

        # writing...
        scrap_csv.writerow({
            'country': country_i, 
            'capital': capital_i,
            'population': population_i,
            'area': area_i
            })

# closing the file to reduce resource consumption        
html_file.close()