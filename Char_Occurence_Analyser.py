import os
import sys

#Variables
i = input("""Entrer text to analyse:
>> """)
list_char = []
ignored_char = {' ',',',"'",'.',':',';','/','?','!'}
occ_char = {}

#List every valid char
for char in i.lower():
    if char not in ignored_char:
        list_char.append(char)

#Count how many time they appear
for char in list_char :
    if char in occ_char:
        occ_char[char] += 1
    else:
        occ_char[char] = 1

#Calcul the appearance rate
occ_char_perc=occ_char.copy()
for char in occ_char:
    occ_char_perc[char] = str(round(occ_char[char] / len(list_char) * 100, 1))

#Display the result
os.system('cls')
print("Char's occurency in the text:")
print("letter   occurence   percentile")
for letter in occ_char:
    print("   " + letter + "         " + str(occ_char[letter]) + "         " + occ_char_perc[letter] + ' %')
input("'ENTER' to leave the script")
sys.exit(0)
