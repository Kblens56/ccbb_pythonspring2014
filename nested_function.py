#!/usr/bin/env python 

# Function one - open sites_simple.csv and name it f ... seems to be names function_one()
def function_one():
	f = open('sites_simple.csv', 'r')
	return f	

# Function two - runs function one and creates striped and separated list of things in file as list of list
def function_two():
	line_list = []
	for line in function_one():
		line_list.append((line).strip().split(','))
	return line_list
	
# Function three - Checks number of things in each line
def function_three():
	for line in function_two():
		if len(line) == 4:
			print len(line)
		else:
			print "incorrect length"
			
print
print 'Is each line 4?'
function_three()
			
# Function Four - to make a list of only observations column without header
def function_four():
	line_list = function_two()
	Observations = []
	for line in line_list[1:]:
		Observations.append(line[1])
	return Observations

function_four()

Observations = function_four()

print
print 'What are the values in the observations column?'
print Observations