#!/usr/bin/env python

result = {}

for line in open('drug2.txt', 'r'):
	name, synonym, dTargets, pubchem = line[:-1].split('\t')
	# Split Sysnonym
	
	sList = synonym.split(',')
	tList = dTargets.split(',')
	for dt in tList:
		if dt == '':
			continue

		# Check /
		modTargets = []
		if dt.find('/') != -1:
			parts = dt.split('/')
			firstItem = parts[0]
			firstItemSub = firstItem[0:len(firstItem)-1]
			for p in parts:
				if p != firstItem:
					p = firstItemSub + p
				modTargets.append(p)
		else:
			modTargets = [dt]

		for t in modTargets:
			if not result.has_key(t):
				newList = [name]
				result[t] = newList
			else:
				result[t].append(name)
	

print 'Drug Target\tDrug Name'
for key in sorted(result):
	entry = key+'\t'
	drugList = ''
	for drug in result[key]:
		drugList = drug+','+drugList
	entry = entry+drugList

	print entry[0:-1]

