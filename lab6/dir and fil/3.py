import os   
main=os.getcwd()
path=input('Choose path: ')
if path[:-1]=="lab":
    for filles in os.listdir(os.path.join(main,path)):
        if os.path.isfile(filles): print(f"{path}- {filles}")
else :
    x=input("chose labs folder: ")
    y=input(f"Choose folder in {x}: ")
    main1=os.path.join(main,x)
    for filles in os.listdir(os.path.join(main1,y)):
        if os.path.isfile(filles): print(f"{x}-{y}- {filles}")
