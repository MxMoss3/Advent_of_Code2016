import pdb

inputfile = open('day_6.txt')
text = inputfile.read()
inputfile.close()


split = text.split('\n')
split.pop()
common = []
broken = [[row[i] for row in split] for i in range(8)]
for x in broken:
	number = x.count(x[0])
	lowest = x[0]
	for y in x:
		if x.count(y) < number:
			number = x.count(y)
			lowest = y
		else:
			pass
	common.append(lowest)
print(common)
