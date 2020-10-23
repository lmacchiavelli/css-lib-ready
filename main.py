import os
listtree = os.listdir("./Elementi")
listtree.remove('.DS_Store')

def mostraAlbero():
	a = 0
	for i in listtree:
		print(a,i)
		a+=1

	x = input('Seleziona sezione da inserire nel css:')
	listtree.pop(int(x))
	mostraAlbero()



print(type(listtree))
print(listtree)
mostraAlbero()