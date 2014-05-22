import re

# is the begining of sequencing file made into a string
str = '>gi|357123948|ref|XP_003563669.1| PREDICTED: protein brittle-1, chloroplastic/amyloplastic-like [Brachypodium distachyon]'

# will look for '>gi' in str
re.findall(r'>gi', str)

# searches for XP_ and then 9 of any digit  and then . and one more digit
search_string = re.search(r'XP_\d{9}.\d', str)

search_string.group()

motifs = ['IRKKAKKRGLK', 'AFDTANKF', 'VNVIRVAPSK', "SSSS"]
seq_string = 'FASVGHKVGVGFPASSSSSGATSSGNPQDPYRKYVSPEAVETSLPVPGDGVGLRGKGKKKAVRIKIKVGNSHLKRLISGG'

for motif in motifs:
    if re.search(motif, seq_string):
        print 'Following motif found:%s' % motif
        
# wont work because the capitalization is not right
new_string = re.sub("predicted", "Synthesized", str)

# this will find any instance of the word predicted regardless of its capitalization
new_string = re.sub('(?i)predicted', "Synthesized", str)

# names reg as this thing
reg = re.compile('>gi', re.IGNORECASE)

f = open('sequences.txt', 'r')

found_list = re.findall(reg, f.read())

f.seek(0)

new_search = re.compile('XP_\d{9}.\d')

with open('sequences.txt', 'r') as f:
	for line in f:
		if re.search(reg, line):
			print line