abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "p", "r", "s", "t", "u", "v", "y", "z"]
for i in abc:
	for j in range(1,10):
		print('"% '+ str(j) + " $ " + str(i) + '": "' + "%" + str(j) + "$" + str(i) + '",')
for i in abc:
	print('"% ' + str(i) + '": ' + '"%' + str(i) + '",')
for i in range(1,10):
	print('"% ' + str(i) + '": ' + '"%' + str(i) + '",')