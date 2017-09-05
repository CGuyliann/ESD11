
print ('Le mot a touver est : T... ')
list = ["T","e","s","t"]
f = 4
m = raw_input ('Entrez une lettre : ')
if m == list[1]:
	print ('Bravo !')
while m != list[1]:
if f == 3:
	print ('Il vous reste 3 essais !')
if f == 2:
	print ('Il vous reste 2 essais !')
if f == 1:
	print ("C'est le derniere essai !")




list = ["T","e","s","t"]
m = raw_input ('Entrez la lettre suivante Te.. : ')
if m == list[2]:
	print ('Bravo !')
else:
	print ('Faux !')

list = ["T","e","s","t"]
m = raw_input ('Entrez la derniere lettre Tes. : ')
if m == list[3]:
	print ('Le mot est "Test". You Win !')
else:
	print ('Faux !')
