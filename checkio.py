#1 All the Same
def all_the_same(elements: List[Any]) -> bool:
    for it in range(len(elements) - 1):
        if elements[it] != elements[it+1]:
            return False
    return True


#2 House Password
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
	
	
#3 The Most Wanted Letter
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


# 4 Time Converter (24h to 12h)
import datetime
def time_converter(time):
    d = datetime.datetime.strptime(time, "%H:%M").strftime("%I:%M %p").lower()
    d = "{}{}.{}.".format(int(d[:2]), d[2:-1], d[-1])
    return d

# 5 Non-unique Elements
def checkio(data: list) -> list:
    return [nonunique for nonunique in data if data.count(nonunique)>1]


# 6 Sort Array by Element Frequency
def frequency_sort(items):
    hmap = {k:items.count(k) for k in items}
    tierList = {k: v for k, v in sorted(hmap.items(), key=lambda item: item[1], reverse=True)}
    return [k for k, v in tierList.items() for i in range(v)]

# 7 Flatten a List
def flat_list(array): 
    n = []
    for i in array:
         if isinstance(i, list):
             n = n + flat_list(i)
         else:
             n.append(i)
    return n

# 8 Long Repeat
def long_repeat(line: str) -> int:
    if len(line) == 0: return 0
    data = [[line[0], 1]]
    for i in range(1, len(line)):
        if line[i] != line[i-1]:
            data.append([line[i], 1])
        else:
            data[-1][1] += 1
    data.sort(key = lambda x: x[1], reverse=True)
    return data[0][1]

# 9 Sun Angle
def sun_angle(time):
    h, m = time.split(":")
    ntime = int(h) * 60 + int(m)
    if  1080 >= ntime >= 360: return (ntime - 360) /4
    else: return "I don't see the sun!"

# 10 Bird Language
def translate(phrase):
    words = phrase.split()
    newwords = []
    for word in words:
        c = 0
        while c < len(word):
            if word[c] in "aeiouy":
                word = word[:c+1] + word[c+3:]
            else:
                word = word[:c+1] + word[c+2:]
            c += 1
        newwords.append(word)
    return " ".join(newwords)

# 11 Pawn Brotherhood
def safe_pawns(pawns: set) -> int:
    res, alph = 0, " abcdefghi"
    for el in pawns:
        def1 = '{}{}'.format(alph[alph.index(el[0]) - 1], int(el[1]) - 1)
        def2 = '{}{}'.format(alph[alph.index(el[0]) + 1], int(el[1]) - 1)
        if def1 in pawns or def2 in pawns:
            res += 1
    return res
