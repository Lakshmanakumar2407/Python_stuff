'''
1. Genearte csv using faker
2.  Parse names from csv
3. Put it into unordered lit in html
'''

# Methodlogy, new try so as to reduce my coding time incosistency

'''
- change cwd
- Create csv file using context manager and write fake name using faker module into it.
- Create a if block to ignore if the csv file is already created
- open the created csv using context manager
- try keeping the file in generator 
- use decorator concept to wrap the names in htmltags
'''

# importing required modules
import csv, random, os
from faker import Faker
fake = Faker()

# changing working directory
os.chdir(r'Python\Python_Basics')
print(os.getcwd())

# creating sample csv file
with open('43.1_csv_names_sample.csv','w', newline='\n') as new_csv:

    # new_csv = csv.writer(new_csv)
    head = ['Name', 'Amount']
    new_csv = csv.DictWriter(new_csv, fieldnames=head, delimiter=',')
    new_csv.writeheader()

    for i in range(20):
        new_csv.writerow({'Name' : str(fake.name()), 'Amount' :str(round(random.uniform(2.00, 5.00),2))})


# opening the created csv file and writing the names to a generator ????
with open('43.1_csv_names_sample.csv', 'r') as csv_read:
    csv_read = csv.reader(csv_read)
    next(csv_read) # ignoring the header row
    # names_list = (line[0] for line in csv_read) # created generator to pass on the list to decortaor class

    # @wrapper_ul
    def append_li(some_string):
        new_string = f'<li>{some_string}</li>'
        return new_string
        # return len(some_generator)

    # opening and writing names in html format...
    with open('43.2_patreon.html','w') as new_html:
        new_html.write('<ul>\n')
        for line in csv_read:
            new_html.write('\t')
            new_html.write(append_li(line[0]))
            new_html.write('\n')
        new_html.write('</ul>')


# def wrapper_ul(some_func):
#     def wrapper_li(*args, **kwargs):
#         print('test')
#         print(f'<li>{some_func(*args,**kwargs)}<\li>')
#     return wrapper_li   



# for name in names_list:
#     print(append_li(name))
# # print(output) 

'''
Didn't use decorator :)
'''