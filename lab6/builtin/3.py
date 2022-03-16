s=input()
def pal(s):
    s_rev=''
    for i in reversed(s):
        s_rev+=i
    if s_rev==s:
        return True
    else : return False
print(f"{s} palindrom -- {pal(s)} ")
