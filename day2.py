with open("input_day2.txt") as f:
	l = [(list(map(int, a.split('-'))), 
		  b[0], 
		  c.strip()
		 ) for a, b, c in (line.split(' ') for line in f.readlines())
	]

solution1 = sum([minmax[0] <= password.count(char) <= minmax[1] for minmax, char, password in l])
print("Solution 1:", solution1)

solution2 = sum([(password[idxs[0]-1]+password[idxs[1]-1]).count(char) == 1 for idxs, char, password in l])
print("Solution 2:", solution2)