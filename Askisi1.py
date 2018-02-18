import random

anagelmenoi_arithmoi=0
for i in range(1000):
  mesos_oros=0
  arithmoi_paiktwn=[[0]*5 for i in range(100)]
  for i in range(100):
    j=0
    help_list=[]
    while j<5:
      x=random.randint(1,80)
      if x not in help_list:
        help_list.append(x)
        arithmoi_paiktwn[i][j]=x
        j=j+1
  help_list=[]
  restnums=[5 for i in range(100)]
  win=False
  lista=[]
  while win==False:
    x=random.randint(1,80)
    if x not in lista:
      lista.append(x)
      mesos_oros+=1
      if x not in help_list:
        help_list.append(x)
        for i in range(100):
          for j in range(5):
            if x==arithmoi_paiktwn[i][j]:
              restnums[i]-=1
          if restnums[i]==0:
            win=True
            winner=i+1
  anagelmenoi_arithmoi+=mesos_oros
print anagelmenoi_arithmoi/1000
