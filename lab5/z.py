import re
a="KBTU-KBTU!"
res=re.search("^KBTU-\d{4}!$" , a)
print(res)