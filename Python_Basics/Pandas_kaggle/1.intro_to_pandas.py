# INTRO TO PANDAS 

# pandas are generaly data handling manipulation module in python

import pandas as pd # usally done this way

# creating dataframe in pandas
dataframe = pd.DataFrame({'Laks':[98,23,4,3,78],'Adi':[34,67,99,100,32]}) # take note of capital letter sin syntax
print(dataframe,'\n')

# creating custom index/row names
dataframe = pd.DataFrame({'Laks':[98,23,4,3,78],'Adi':[34,67,99,100,32]}, index = ['Physics','Maths','Chemistry','English','Tamil']) 
print(dataframe,'\n')

# creatingf series in pandas
series = pd.Series([1,2,3,4,5], index = ['one','two','three','four','five'],name = 'Test') # capital letter syntax
print(series)

# usally we won't be working with this kind of toy data. 
# we will work with large amount of data with millions and billion of values. that is where pandas shines

# these kind of data are mostly stored in csv (comma - seperated values ) or excel or someother type

data = '../file path' # no file path here 
data_in_table = pd.read_csv(data) # read_csv is the syntax
# data_in_table onverts the csv data into data_frames

# to see the size of data_frame
print(data_in_table.shape)

# to see only the top 5 rows of the data frame
print(data_in_table.head)

# to see only last 5 rows of the data frame
print(data_in_table.tail)

