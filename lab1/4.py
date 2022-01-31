def toFixed(number, digits=0):
        return f"{number:.{digits}f}"

number=int(input())     # 3032/1024=2.489646488 
BorK=input()
if BorK=="k":
    number/=1024
    how=int(input())
    print(toFixed(number,how))
else:
    print(number*1024)
