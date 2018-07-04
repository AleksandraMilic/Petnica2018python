import random

string = open("ime.txt", "r")
string2 = string.read()
string3 = random.choice(string2.split())
lenstring = len(string3)
#print(lenstring)
underline = lenstring * '_ '
print(underline)
tries = 6
print(tries)

def func(letter):
    place_underline = input("unesi broj crte")
    letter = input("unesi slovo")
    place_underline2 = int(place_underline)
    count = 6
	while count <= 6:
		if letter == string[place_underline2]:
			underline2 = underline	
			underline[place_underline2] = letter
			print(underline)
		else: 
			tries2 = tries - 1
			print(underline)
			print(letter)
			print(tries2)
