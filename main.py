import os
listtree = os.listdir("./Elementi")
listtree.remove('.DS_Store')


from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('./Elementi/form') if isfile(join('./Elementi/form', f))]



def mostraAlbero():
	a = 0
	for i in listtree:
		print(a,i)
		print(onlyfiles)
		a+=1

	x = input('Seleziona sezione da inserire nel css:')
	#listtree.pop(int(x))
	
	mostraAlbero()



print(type(listtree))
print(listtree)
mostraAlbero()