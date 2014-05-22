# coding: utf-8

# import pandas which will be a much nicer interface to do graphing with and work with large excel sheets
import pandas

cd documents/ccbb_pythonspring2014/

# to open sites simple with panas as an excel file and name it xl
xl = pandas.ExcelFile('sites_simple.xlsx')

# to see the names of the sheets in the excel document
xl.sheet_names

# to parse out sheet 1 and name it df
df = xl.parse('Sheet1')

# will show sheet one as is parsed
df

# will show only the top of 'df' the 2 indicates up to row 2
df.head(2)

# to show a particular row in this case row 0 (if give df.ix only one number it will grab a row)
df.ix[0]

# gives first row second column, first number indicates row, second indicates column
df.ix[1,2]

# colon give all of the rows and then the 3 gives the column
df.ix[:,3]

#above gives rows upto and inculding 2 of collumn 3
df.ix[:2,3]

# want to make names names and then be able to use them so name the index column 
# which is column 0 here and name the header which is also 0 here (not sure what header is)
df = xl.parse('Sheet1', index_col = 0, header = 0)
df
# names of rows and columns can now call data within those by the names

# to call the row name "Lake_Creek"
df.ix['Lake_Creek']

# to call the column observations
df.ix[:,'Observations']

# can bind number of species to a variable (here to variable a), it will still be ordered unlike a dictionary
a = df.ix[:,'Species']
a

#actions can then be taken on the numbers within that 
sum(a)
a.mean()

# bind the number of observations to another variable
b = df.ix[:,"Observations"]
b
sum(b)

# then can do calculations using those numbers together easily
sum(b)/sum(a)
sum(a)/sum(b)

# can assign only a portion of the numbers in observations to a variable
b = df.ix[:2,"Observations"]
b
sum(b)
sum(a)/sum(b)

# import sites_complicated and called it xl_c
xl_c = pandas.ExcelFile('sites_complicated.xlsx')
xl_c

# parse out sheet 1 and name df_c
df_c = xl_c.parse('Sheet1')
df_c

#NaN means not a number (empty excel box in this case)
#pandas ingnores NaN valuse

#above to add expenditure or collumn #3 and ignored NaN values
df_c.ix[:,3].sum()

df_c.ix[:,3].mean()
df_c.ix[1,3]
df_c.ix[1,3] = 0
df_c

# import numpy so can apply map
import numpy

# a map of what values are numbers and which are not
df_c.applymap(numpy.isreal)

# to group things together that are next to eachother and are the same
grouped = df_c.groupedby('Expenditure')
grouped = df_c.groupby('Expenditure')
grouped.groups
df_c = xl.parse('Sheet1', index_col = 0)
grouped = df_c.groupby('Expenditure')
grouped.groups
df_c.groupby(['Expenditure']).sum()
