try:
  arithmos=int(raw_input('���� ��� ���� ������\n'))
  if arithmos>0:
    list1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    list2=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    latinikos_arithmos=""
    for i in range(13):
      latinikos_arithmos+=list2[i]*int(arithmos/list1[i])
      arithmos-=int(arithmos/list1[i])*list1[i]
    print latinikos_arithmos
  elif arithmos==0:
    print '�� ������� ��� ����� ������ ��� �� �������������� �� 0, ���� ����� ������ �� ���� nulla'
  else:
    print '�� ��������� ������� ��� ������� ����� ���������� ����������'
except ValueError:
  print "������� ���� ��������"
