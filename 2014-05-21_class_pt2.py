import pandas
import numpy

cd documents/ccbb_pythonspring2014/

# open sites_complicated in pandas as an Excell file and then parse out Sheet 1
xl_c = pandas.ExcelFile('sites_complicated.xlsx')
df_c = xl_c.parse('Sheet1')

# how to output file in pandas
# to write file in pandas and make csv will be called output.csv
outfile = open('output.csv', 'w')
df_c.to_csv(outfile)
outfile.close()

# to import all "*" from pandas
from pandas import *

# now can write excell file from pandas
writer = ExcelWriter('output.xlsx')
df_c.to_excel(writer, 'Sheet1')

## now moving onto ploting

#import all "*" from ggplot
from ggplot import *

# open and parse sites simple
xl = pandas.ExcelFile('sites_simple.xlsx')
df = xl.parse('Sheet1', index_col = 0, header = 0)

# make a plot saying what data will use etc
my_plot = ggplot(df, aes(x = 'Expenditure', y = 'Species')) + geom_point() + xlim(0,350) + ylim(0,25)

# to see plot
my_plot

#to save the plot
# can save while looking at the plot by pushing the save button
# or can save it programaticaly
ggsave(my_plot, "demo_plot", "png")

# now we will switch to working with a very large excel document
# to import the data and name it big_matrix
big_matrix = pandas.read_csv('big_matrix.csv')

# to see the beginning of "big_matric"
big_matrix.head()

# this is what I see, April saw several of the first columns I assume this is a setting thing
Out[37]: 
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5 entries, 0 to 4
Columns: 1001 entries, 0 to 0.5034046342
dtypes: float64(1000), int64(1)

# to import te dat in a slightly differnt way ... not sure why the collumn now says entries 0 to 100 instead of 1 to 0.5
big_matrix = pandas.read_csv('big_matrix.csv', index_col=None, header=None)
big_matrix.head()

Out[40]: 
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5 entries, 0 to 4
Columns: 1001 entries, 0 to 1000
dtypes: float64(1000), int64(1)

# to add a 1002nd collumn that will say Me for the first 250 rows and then My_Labmate for the rest of the rows
big_matrix['1002'][0:250] = 'Me'
big_matrix['1002'][250:] = 'My_Labmatee'

# to display a sample of what column 1002 looks like
big_matrix['1002']

# this is what it looks like
Out[49]: 
0     Me
1     Me
2     Me
3     Me
4     Me
5     Me
6     Me
7     Me
8     Me
9     Me
10    Me
11    Me
12    Me
13    Me
14    Me
...
485    My_Labmatee
486    My_Labmatee
487    My_Labmatee
488    My_Labmatee
489    My_Labmatee
490    My_Labmatee
491    My_Labmatee
492    My_Labmatee
493    My_Labmatee
494    My_Labmatee
495    My_Labmatee
496    My_Labmatee
497    My_Labmatee
498    My_Labmatee
499    My_Labmatee
Name: 1002, Length: 500, dtype: object

# make a plot where me and my labmates data are differnt colors on a scatterplot
overlay = ggplot(aes(x=big_matrix.ix[0:499,2], y = big_matrix.ix[:,1], color='1002'), data=big_matrix) + geom_point() +geom_jitter()  + ylab("Y Axis") + xlab("X Axis") +ylim(0,1) + xlim(0,1) + theme_bw()

# to see plot
overlay