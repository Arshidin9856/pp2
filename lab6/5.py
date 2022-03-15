import os
# path=os.path.join(os.getcwd(),input("Print rest of current working directory: "))
# if os.path.exists(path):
#     print("Path exist")
# else:print('Wrong path')
x=input("Write path: ")
if os.path.exists(x):
    print("Path exist")
    print(os.path.basename(x))
    print(os.path.dirname(x))

else:print('Wrong path')
