s=input() #FIVSIX+NINNINNINNIN ==> 56+9999=10055 ==> ONEZERZERFIVFIV
l=s.split("+")
d={ 'ONE' :'1','TWO' :'2','THR': '3','FOU': '4',"FIV" :'5','SIX' :'6','SEV' :'7','EIG' :'8','NIN': '9','ZER' :'0' }
l1=[]
l2=[]
sum=0
def stringTOnumber(l):
    i=l[0]
    p=0
    for c in range(1,len(i)+1):
        if c%3==0:
            l1.append(i[p:c])
            p=c
    z=l[1]
    p=0
    for c in range(1,len(z)+1):
        if c%3==0:
            l2.append(z[p:c])
            p=c
    d1=''
    d2=''
    for q in l1:
        for w in d.keys():
            if q==w:
                d1+=d.get(w)    
    for q in l2:
        for w in d.keys():
            if q==w:
                d2+=d.get(w)    
    global sum
    sum=int(d1)+int(d2)    

stringTOnumber(l)


def numberToresult(sum):
    res=''
    for i in str(sum):
        for w,e in d.items():
            if i==e:
                res+=w
        
    print(res)
numberToresult(sum)
