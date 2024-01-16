# along with practicing csv module we alos perfrom some data analysis

import csv
import os

os.chdir('Python/Python_Basics/')

row_count = 0

with open('39.1_jobs_in_data.csv', 'r') as sample_csv_read:
    csv_read = csv.reader(sample_csv_read)
    
    with open('39.2_jobs_in_data_copy_tab.csv', 'w', newline= '') as sample_csv_write: # if newline is not added the new file will be created with '\n' between alternating character
        csv_write = csv.writer(sample_csv_write, delimiter='\t')

        for line in csv_read:
            row_count += 1
            csv_write.writerow(line)

os.remove('39.2_jobs_in_data_copy_tab.csv') # remove this line to execute the above code...

# print(sample_csv_read.closed)

# DictReader is more usefull corey says...
with open('39.1_jobs_in_data.csv') as csv_for_analysis:
    csv_read = csv.DictReader(csv_for_analysis)
    data = list(csv_read)

    # Filtering out only the values I need... - 'work_year', 'job_category', 'salary_in_usd', 'company_location'
    work_year = [line['work_year'] for line in data]
    salary_in_usd = [line['salary_in_usd'] for line in data]
    company_location = [line['company_location'] for line in data]

    with open('39.2_jobs_in_data_filtered.csv','w', newline='') as sample_csv_write:
        file_head = ['work_year', 'salary_in_usd', 'company_location']
        filtered_csv = csv.DictWriter(sample_csv_write, fieldnames = file_head, delimiter='\t' )
        filtered_csv.writeheader()

        for line in data:
            del (
                line['job_category'],
                line['job_title'], 
                line['salary_currency'], 
                line['salary'], 
                line['employee_residence'], 
                line['experience_level'], 
                line['employment_type'], 
                line['work_setting'], 
                line['company_size']
                )
            filtered_csv.writerow(line)

# Combining the filtered data into dict
filtered_dict = {}
for i in range(row_count-1): # row_count-1 because it counts the total rows including the header_rows
    # print(i, work_year[i], salary_in_usd[i], company_location[i])
    filtered_dict[i] = [work_year[i], salary_in_usd[i], company_location[i]]

# Finding average mean salary...
def mean_salary(some_dict):
    sum_of_all_salary = 0
    for i in range(len(some_dict)):
        sum_of_all_salary += int(some_dict[i][1])
    mean = sum_of_all_salary/len(some_dict)
    return round(mean)

def most_year_count(some_dict):
    year = [int(year[0]) for year in some_dict.values()]

    # creating a dictonary to count occurences..
    count_dict = {}
    for val in year:
        if val in count_dict:
            count_dict[val] += 1
        else:
            count_dict[val] = 1
    # min_year = int(min(year))
    # max_year = int(max(year))
    # year_count_dict = {}
    # for index_year in range(min_year, max_year+1):
    #     year_count_dict[index_year] = 0
    #     max_count = 0
    #     for val in year:
    #         if int(val) == index_year:
    #             year_count_dict[index_year] += 1
    #         if year_count_dict[index_year] > max_count:
    #             max_count = year_count_dict[index_year] 
    '''Ignore my above stupidity'''
    reverse_mapp = {value: key for key, value in count_dict.items()}
    return reverse_mapp[max(reverse_mapp.keys())]

def most_country_count(some_dict):
    country = [val[2] for val in some_dict.values()]
    count_dict = {}
    for country in country:
        if country in count_dict.keys():
            count_dict[country] += 1
        else:
            count_dict[country] = 1
    return len(count_dict), max(count_dict, key=count_dict.get)


print(mean_salary(filtered_dict))
print(most_year_count(filtered_dict))
print(most_country_count(filtered_dict))