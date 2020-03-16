# Home

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

# 12 Xs and Os Referee
def checkio(game_result: List[str]) -> str:
    for i in range(3):
        if game_result[i][0] == game_result[i][1] == game_result[i][2]:
            return game_result[i][0]
        elif game_result[0][i] == game_result[1][i] == game_result[2][i]:
            return game_result[0][i]
        elif game_result[0][0] == game_result[1][1] == game_result[2][2]:
            return game_result[0][0]
        elif game_result[0][2] == game_result[1][1] == game_result[2][0]:
            return game_result[0][2]
    return "D"
# 13 Warriors
class Warrior:
    hp, at = 50, 5
    @property
    def is_alive(self):
        return self.hp > 0
        
class Knight(Warrior):
    at = 7
    
def fight(unit_1, unit_2):
    while True:
        unit_2.hp -= unit_1.at
        if not unit_2.is_alive: return True
        unit_1.hp -= unit_2.at
        if not unit_1.is_alive: return False

# 14 Restricted Sum
res = 0
def checkio(data):
    global res
    exec("global res; res = " + '+'.join(map(str, data)))
    return res

# 15 Count Consecutive Summers
def count_consecutive_summers(num):
    start, res = 0, 0
    numbers = [i for i in range(1, num+1)]
    while start < num:
        for i in range(1, num + 1):
            if sum(numbers[start:start+i]) == num:
                res += 1
                start += 1
            elif sum(numbers[start:start+i]) > num:
                start += 1
                break
    return res


# O Reilly

# 16 Median
def checkio(data):
    newdata, leng = sorted(data), len(data)
    if leng % 2 == 0:
        return (newdata[int(leng/2)] + newdata[int(leng/2 - 1)])/2
    return newdata[int(leng/2)]

# 17 How to Find Friends
def check_connection(network, first, second):
    connections = [p.split("-") for p in network]
    allFriends = []
    nextToCheck = [first]
    while len(nextToCheck) > 0:
        tmpl = []
        connToRemove = []
        for ch in nextToCheck:
            for pair in connections:
                if ch in pair:
                    tmpl.append(pair[pair.index(ch) - 1])
                    connToRemove.append(pair)
            for p in connToRemove:
                try: 
                    connections.remove(p)
                except ValueError:
                    pass
        nextToCheck = tmpl
        allFriends += nextToCheck
    return True if second in allFriends else False

# 18 Cipher Map
import numpy as np
def recall_password(cipher_grille, ciphered_password):
    grille = np.array([list(l) for l in cipher_grille])
    res = ''
    for i in range(4):
        for (gl, pl) in zip(grille, ciphered_password):
            for g, p in zip(gl, pl):
                if g == "X":
                    res += p
        grille = np.rot90(grille, k=-1)
    return res
