# coding: utf-8

# to open sites simple.csv as a read only file
f = open('sites_simple.csv', 'r')
f

# to read all the lines and show them
f.readlines()

# to append each line to line_list
line_list = []
for line in f:
    line_list.append(line)
    
line_list

# didn't work because were at the end of the document because we did readlines so there was nothing to append and had to repeat
f.seek(0)
for line in f:
    line_list.append(line)
    

# to append the items to line list but strip off training white space and split items at comas to make a list of lists
line_list = []
f.seek(0)
for line in f:
    line_list.append((line).strip().split(','))
    
# will print column 3 basically
line_list
for line in line_list:
    print line [3]
    
# to see if there were the corect number of items in the list
for line in line_list:
    if len(line) == 4:
        print len(line)
        
# build a dictionary to see how much it costs to visit each site, 0 = key and 3 = value for that key
money_dictionary = {}
for line in line_list:
    money_dictionary[line[0]]=line[3]

money_dictionary
money_dictionary["Los_Alamos"]
# see that dictonary does not maintain ordering of list it came from
# should use keys to look up info once in dictionary

# to get rid of the header in the dictonary or notput it in
money_dictionary = {}
for line in line_list[1:]:
    money_dictionary[line[0]]=line[3]
    
money_dictionary

# to create a file and then write a sentece in it using the dictionary
# then closed file which will actually write it to that file
# otherwise it will not be writen to it
outfile = open('out.txt', 'w')
outfile
for item in money_dictionary.keys():
    outfile.write('It cost %s dollars to sample %s location' %(money_dictionary[item], item) +'\n')
    outfile.close()
 
# here the file is created but not closed so there is nothing writen to it until   
for item in money_dictionary.keys():
    outfile.write('It cost %s dollars to sample %s location' %(money_dictionary[item], item) +'\n')
    
for item in money_dictionary.keys():
    outfile.write('It cost %s dollars to sample %s location' %(money_dictionary[item], item) +'\n')
    
outfile = open ('out.txt', 'w')
for item in money_dictionary.keys():
    outfile.write('It cost %s dollars to sample %s location' %(money_dictionary[item], item) +'\n')
    
# here where it is closed
outfile.close()

# prints values in observations column out but not the title observatios
line_list[0]
for line in line_list[1:]:
    print line [1]
        

# Creates a list Observations that has all the values that were in onservations
Observations = []
for line in line_list[1:]:
    Observations.append(line[1])
    
Observations

# to make a new txt file called ner_file and write 'my data' into it
with open('new_file.txt', 'w') as new_file:
    new_file.write('my data')
    
# To make and populate the list at once
value_list = [line[2] for line in line_list]
value_list

# to open sites complicated and make complex list
complex = open('sites_complicated.csv', 'r')
complex_list = []
    
for line in complex:
    complex_list.append(line.strip().split(','))    
complex_list

# try and accept statements
# sets up something you will try to do and sets up some exceptions that you can have
# will test if something is a number. has to change line[1] to intiger becasue it is a string
# a non-numbr cannt have 1 added to it 
      for line in complex_list:
    try:
        int(line[1]) + 1
        print line[1]
    except ValueError:
        print "This is not a number:", line[1]
        

# os allows to interact with operating system of computer
import os

#to define get list function which will get a list of files that ende with .md
def get_list(): 
    file_list = []
    for file in os.listdir('.'):
        if file.endswith('.md'):
            file_list.append(file)
    print file_list
    return file_list

# the function is only executed when get_list() is typed
get_list()

# define function use_files
def use_files():
    files = get_list()
    for file in files:
        print file
        
use_files()

# if define get_list function without the return then the use _files no longer works (see below)
def get_list(): 
    file_list = []
    for file in os.listdir('.'):
        if file.endswith('.md'):
            file_list.append(file)
    print file_list
    
get_list()
use_files()

# returns are the way functions exit from themselves
#functions can also take input

my_files = os.listdir('.')
def get_list(list):
    for file in list:
        if file.endswith('.md'):
            print 'yay'
            
# this will put whatever was indicated as the my_files variable into the get_list function in the brackets where it says list
get_list(my_files)
