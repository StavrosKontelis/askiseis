import string
keimeno_xristi=raw_input("Δώσε μου κείμενο")
krypto_keimeno_xristi=[]
lista_kefalewn=list(string.ascii_uppercase)
lista_mikron=list(string.ascii_lowercase)
lista_krypto_kefalewn=['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
lista_krypto_mikron=['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']


for i in keimeno_xristi:
  Flag=False
  thesi=0
  for y in lista_kefalewn:
    if y==i:
      krypto_keimeno_xristi.append(lista_krypto_kefalewn[thesi])
      Flag=True
    thesi+=1
  thesi=0
  for y in lista_mikron:
    if y==i:
      krypto_keimeno_xristi.append(lista_krypto_mikron[thesi])
      Flag=True
    thesi+=1
  if Flag==False:
    krypto_keimeno_xristi.append(i) 
teliko_keimeno=''
for y in krypto_keimeno_xristi:
  teliko_keimeno=teliko_keimeno+y
print teliko_keimeno
