# SLICING, INDEXING and ASSIGNING in PANDAS

import pandas as pd

# don not runt his file. consider some hypothetical data =frame is already in the project

# dataframes has column names. this can be shows through
columns = dataframe.columns

# to access only a specific column in the dataframe
choosen_column = dataframe.columnname
# or
choosen_column = dataframe['columnname1','columnname2']
# second syatx is better because you can pass multiple column names 
# this can also be done in 1st syntax like this..
column_list = ['columnname1','columnname2','columnname3']
choosen_column = dataframe.column_list

# to access a specific in the choose column...
dataframe.column_list[0,1,2,3]
# or
list = list(range(100))
dataframe.column_list.list
# or
dataframe['columnname1'][1,2,3,4]



### Indexing ###

# there are usually two indexing operators in python
# simple can indexing can also be done directly

dataframe[0]

# First indexing operator - iloc[] - index based selection

dataframe.iloc[0] # take note of brackets

# both the indexinf operator are ROW-FIRST ; COLUMN-SECOND
# so to access a specif ccolum using iooc
dataframe.iloc[:, 0] # access first column

# for finer control
dataframe.iloc[0:100,[0,11,3,4]] # prints rows from '0' to '99' and columns with index 0,11,3,4
# -tive indexing can also be used
dataframe.iloc[-5:,1]


# Second indexing operator  - loc[] - label based selection
# In this paradigm, it's the data index value, not its position, which matters.
dataframe.loc[0,'columname1']
dataframe.loc[:,['columnname1','columnname2','columnname3']]
 # the main differeence betwen iloc and loc is when indexing rows like 0:100...
# iloc give you rows from 0 to 99 (100 values)
# loc gives you rows from 0 to 100 (101 values)


### Conditional Selection ###
dataframe.columname1 == 'selection1' 
# the above code returns boolean seriess...
# when this boolean series is passed to loc it prints the values which is true.. Imporatnt
dataframe.loc[dataframe.columname1 =='selction1']

# to combine multiple conditionals
dataframe.loc[((dataframe.columname1 == 'selection1') & (dataframe.columname == 'selection2')) | (dataframe.columname >= decisioninteger)]
# & - and operator
# | - or operator

# Pandas has a few builtin conditionals two of which are used below

# isin()
# isin is lets you select data whose value "is in" a list of values
dataframe.loc[dataframe.columname1.isin(['selection1','selection2'])]
# take note of brackets

# isnull() and notnull()
# These methods let you highlight values which are (or are not) empty (NaN)
dataframe.loc[dataframe.columname1.notnull()]


### Assigning Data ###
dataframe['new_columname'] = 'that_column_value'
dataframe['new_columname'] = range(len(dataframe),0,-1)