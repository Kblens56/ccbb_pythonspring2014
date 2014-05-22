#!/usr/bin/env python 

last_name = ['m', 'a', 'r', 't', 'i', 'n', 'e', 'z', '-', 'f', 'o', 'n', 't', 's', '3', '0', '5']
numbers = []
letters = []
other = []

if type(last_name) == list:
	for object in last_name:
		if object.isdigit() == True:
			numbers.append(object)
		elif object.isalpha() == True:
			letters.append(object)
		else:
			other.append(object)


	#Should fail to test if the starting list 'last_name' is only numbers or letters:
	print "1) is last name only numbers?"
	for object in last_name:
		if object.isdigit() == False:
			print "contains non numbers"
			break
			
		
	print "2) is last name only letters?"
	for object in last_name:
		if object.isalpha() == False:
			print "contains non letters"
			break


	#Should pass after sorting to test if the sorted lists 'numbers' is only numbers:
	print "3) is numbers only numbers?"
	for object in numbers:
		if object.isdigit() == False:
			print "contains non numbers"
			break
		

	#Should pass after sorting to test if the sorted lists 'letters' is only letters:
	print "4) is letters only letters?"
	for object in letters:
		if object.isalpha() == False:
			print "contains non letters"
			break
    	
else:
	print "not a list, cannot exicute"