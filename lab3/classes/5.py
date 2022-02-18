owners={'1':5000,'2':10000,'3':100}
class Account:
    def __init__(self,owner):
        self.owner=owner
    def deposit(self,money):
        for x,y in owners.items():
            if self.owner==x:
                y+=money
                print(f'Now you have {y}')
    def withdraw(self,money):
        for x,y in owners.items():
            if self.owner==x:
                if y>=money:
                    y-=money
                    print(f'Now you have {y}')
                else : print('you dont have so much')
    
p=Account(input('Write your name\n'))
c=input('do you want deposit\n')
if c=="Yes":
    p.deposit(int(input('How many\n')))        
elif c=='No':
    d=input("do you want withdraw?")
    if d=="Yes":
        p.withdraw(int(input('How many\n')))
    else: 
        print ("Goodbue")
