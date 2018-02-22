import string

#αυτη ειναι η αρχη της 4ης ασκησης μου(10),δεν προλαβα να την τελειωσω,
#,θα ηθελα να μου διορθώσετε παρακαλω το πρωτο κομματι καθως εχω κανει
#λαθος(βαζει το πρώτο στοιχειο του πινακα μονο του) και θα ηθελα
#να δω τον τροπο που θα το λυνατε


#with open ("C:/Users/User/Desktop/fileidk.txt","r") as myfile:
#	keimeno_xristi=myfile.read().replace('\n','')
with open ("C:/Users/User/Desktop/fileidk.txt","r") as myfile:
		keimeno_xristi=myfile.read().replace('.','')
print keimeno_xristi
lista_triadwn=[]
x=0
z=1
leksi=''
triada_leksewn=[]
for i in keimeno_xristi:
	if i!=' ':
		leksi+=i
	elif i==' ':
		x=0
		flag=False
		for y in leksi:
			if y in string.ascii_uppercase:
				flag=True
		if flag==False:
			z+=1
			if z>2:
				lista_triadwn.append(triada_leksewn)
				z=0
				triada_leksewn=[]
			triada_leksewn.insert(z,leksi)
			leksi=''
			
		else:
			leksi=''
		print lista_triadwn


