"""
TASKS....

1. Scrap the website money control for nifty50.
2. Store each stock in separate csv with name, ltp, volume.
3. Scrapp daily using windows scheduler and keep  updating regularly.
4. If new stock breaks into top 100, create an sepearte file for it and send email to myslef.
5. Log when the data is scrapped....
6. Use functions in your code, not like previous ones,
"""

import os, datetime, requests, csv, json
from bs4 import BeautifulSoup

# declare all the variable here....

# variable for scrapp
url = "https://www.moneycontrol.com/markets/indian-indices/changeTableData"


# Starting code here

os.chdir(os.getcwd()+'\\Python\\Python_Basics\\Web_scrapping')

# session = requests.session()

def initial_request(some_link,tab_val):
    parameters = {
    'exName':'N',
    'indicesID':'9',
    'selTab':tab_val,
    'selPage':'marketTerminal',
    'classic':'true'
    }
    response = requests.get(some_link, params= parameters)
    
    if response.status_code<=400:
        soup = BeautifulSoup(response.text,'lxml')
        with open('temp.txt','w',encoding='utf-8',newline='') as temp:
            temp.write(soup.prettify())
        return soup
    else:
        print('Error')


def filter_data(soup_object, *args):

    # parse through all the html in soup_object and filter out all unwanted data and create a generator
    generator_list = (a.text for a in soup_object.find_all('td') if a.text[0]!='\n')
    temp_dict = {}
    count = 0

    # create a dict with stock name as key and last traded price and volume as values...
    for val in generator_list:
        if val[0].isalpha():
            temp_dict[val] = []
            temp_key = val
        for num in args:
            if count%10 == num-1:
                temp_dict[temp_key].append(val)
        count += 1

    return temp_dict

def dict_combiner(*args):
    
    # Create a new dict
    combined_dict = dict()

    # this is gpt code, my messy code is below. 
    # this is such a beautiful code... damn...
    for diction in args:
        for key,value in diction.items():
            if key in combined_dict:
                combined_dict[key] += value
                combined_dict[key].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            else:
                combined_dict[key] = value

    
    
    return combined_dict

def data_storing(some_dict):
    # os.chdir(os.getcwd()+'\\Python\\Python_Basics\\Web_scrapping')
    try:
        os.mkdir('Stock_data')
    except:
        pass
    finally:
        os.chdir(os.getcwd()+'\\Stock_data')
        print(os.getcwd())
    for key,value in some_dict.items():
            with open(f'{key}_historical.csv','a',newline='') as stock_csv:

                stock_csv_writer = csv.writer(stock_csv)

                if os.path.getsize(f'{key}_historical.csv') == 0:
                    filehead= ['LTP','Volume', 'P/E','D/E','EPS(Rs.)', 'ROE%','logged at']
                    stock_csv_writer.writerow(filehead)

                stock_csv_writer.writerow(value)


def main():

    # getting the overview data
    soup = initial_request(url,'o')
    clean_dict_overview = filter_data(soup,2,5)

    # getting the fundamental data
    soup = initial_request(url,'f')
    clean_dict_fundamental = filter_data(soup, 3,4,5,10)
    
    final_dict = dict_combiner(clean_dict_overview,clean_dict_fundamental)
    # print(final_dict)

    new_dict = {}
    stk = 'Axis Bank'
    new_dict[stk] = final_dict[stk]
    # print(new_dict)

    data_storing(new_dict)


if __name__ == '__main__':
    main()


'''
My notes - thinking and mistakes I did

# select the dict with longest length
    # dict_len = [len(dict0) for dict0 in args ]
    # length = 0
    # for dict0 in args:
    #     if len(dict0)>length:
    #         length = len(dict0)
    #         long_dict = dict0
    # check if key in longest dict is in other dicts
    # for key in long_dict:
    #     combined_dict[key] = long_dict[key]
    #     print (combined_dict)
    #     for dict0 in args:
    #         if key in dict0:
    #             if long_dict[key]==dict0[key]:
    #                 continue
    #             else:
    #                 combined_dict[key] += dict0[key]
    #                 # print (combined_dict)
                
    MY THINKING

    How to combine two or more dicts??

    1. create a new dict which will store the combined dicts
    2. select the dict with longest length
    3. check if the key in the longest dict is in other dicts
        3.1 if yes combines the values of the key (here since they are both of same data structure list they can smply be added)
        3.2 if not just add the key to the new dict

    WHAT WENT WRONG WITH MY THINKING?

    - I thought of slecting the longest dict from the given dicts and then checking the remaining dict against that
    - This process involves two computation and numerous loops

    * what gpt did was first pass the given and then iterate over the other dict and check if the values are present if yes append if not add

'''