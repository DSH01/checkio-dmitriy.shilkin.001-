#1 
def all_the_same(elements: List[Any]) -> bool:
    for it in range(len(elements) - 1):
        if elements[it] != elements[it+1]:
            return False
    return True

#2 
def checkio(data):
	up, low, integer, leng = 0, 0, 0, 0
	for symbol in data:
		if type(symbol) == str and symbol.isupper():
			up = 1
		if type(symbol) == str and symbol.islower():
			low = 1
		if symbol.isdigit():
			integer = 1
	if len(data) > 9:
		leng = 1
	if leng + up + low + integer == 4:
		return True
	else:
		return False
	
#3
def checkio(text: str) -> str:
	all = {}
	for letter in text.lower():
		if letter.isalpha():
			if letter not in all:
				all[letter] = 1
			else:
				all[letter] += 1
	maxvalue = max(all.values())
	finalall = []
	for it in all.items():
		if it[1] == maxvalue:
			finalall.append(it[0])
	return sorted(finalall)[0][0]
