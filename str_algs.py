def per(str):
	str2 = ""
	for i in range(len(str)):
		str2 += str[-i-1]
	return str2
	
str = input()
strn = per(str)
print(strn)