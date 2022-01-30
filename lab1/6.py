a=int(input())
list=[]
for i in range(0,a):
    c=int(input())
    list.append(c)
#print (list)
for i in range(0,a):
    if list[i]<=10 and list[i]>=0:
        print('Go to work!')
    elif list[i]>10 and list[i]<=25:
        print('You are weak')
    elif list[i]>25 and list[i]<=45:
        print('Okay, fine')
    elif list[i]>45 :
        print("Burn! Burn! Burn Young!")
   