def is_it_palindrom(s):
    scopy=''
    for i in range(len(s),0,-1):
        scopy+=s[i-1]

    if scopy==s:
        print("yes")
    else: print("no")


is_it_palindrom(input())