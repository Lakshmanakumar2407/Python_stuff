from bs4 import BeautifulSoup
import requests, os, time, csv

# changing working directory..
os.chdir('Python\\Python_Basics\\Web_Scrapping')

# declaring urls
main_url = 'https://www.scrapethissite.com/'
url = 'https://www.scrapethissite.com/pages/forms/'

# # requesting html...
source = requests.get(url).text
# enc = requests.get(url).encoding

# parsing the source throuh beautiful soup
soup = BeautifulSoup(source,'lxml')

# since this web page has multiple pages, accessing the pagination and storing the urls in a list
pagination = soup.find('ul', class_='pagination')
urls = []
for href in pagination.find_all('a'):
    str_dummy = href.get('href')
    if (href.get('aria-label')) == 'Next':
        break
    else:
        urls.append(main_url + str_dummy)

# declating empty list to store dictionaries of team and its data
team_list =[]

# looping through each urls and scrapping the table data
for url in urls:
    time.sleep(2) # pausing the loop so as not to overload their webpage

    source = requests.get(url).text
    # print(source) # - checkpoint

    soup = BeautifulSoup(source,'lxml')
    # print(soup) # - checkpoint

    table_container_ = soup.find('table', class_='table')

    for team in table_container_.find_all('tr', class_='team'):
        empty_dict = dict()

        team_name = team.find('td', class_='name').text
        team_year = team.find('td', class_='year').text
        team_wins = team.find('td', class_='wins').text
        team_losses = team.find('td', class_='losses').text
        team_ot_losses = team.find('td',class_='ot-losses').text
        
        # has two classes so had to do it like this, if condition can also be used but employed EFAP
        try:
            team_win_percent = team.find('td',class_='pct text-success').text
        except AttributeError:
            team_win_percent = team.find('td',class_='pct text-danger').text

        team_gf = team.find('td',class_='gf').text
        team_ga = team.find('td',class_='ga').text

        try: 
            team_success = team.find('td',class_='diff text-success').text
        except AttributeError:
            team_success = team.find('td',class_='diff text-danger').text

        fieldhead_val = [team_name,team_year,team_wins,team_losses,team_ot_losses,team_win_percent,team_gf,team_ga,team_success]
        fieldhead_name = ['team_name', 'team_year', 'team_wins', 'team_losses', 'team_ot_losses', 'team_win_percent', 'team_gf', 'team_ga', 'team_success']

        i = 0
        # stuck in this area so as to pass the dictionary key names as the variable name. didn'tknow how to do it. did this code 
        # with the help of gpt. Learned new function zip() - generator
        for key,val in zip(fieldhead_name,fieldhead_val):
            i+=1
            empty_dict[key] = val.strip()

        team_list.append(empty_dict)


# writing the data to csv            
with open('02_scrapped_hockey_list.csv','w', newline='') as csv_write:
    col_names = ['team_name', 'team_year', 'team_wins', 'team_losses', 'team_ot_losses', 'team_win_percent', 'team_gf', 'team_ga', 'team_success']
    csv_write = csv.DictWriter(csv_write,fieldnames = col_names, delimiter = '\t')
    csv_write.writeheader()
    for team in team_list:
        csv_write.writerow(team)