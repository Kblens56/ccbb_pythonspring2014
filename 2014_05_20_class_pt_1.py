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