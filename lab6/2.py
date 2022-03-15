import os   
main=os.getcwd()
def listall(MY_DIR, otstup):
    for item in os.listdir(MY_DIR):
        path=os.path.join(MY_DIR,item)
        if os.path.isdir(path):
            print('Dir','---'*otstup,f'{item}')
            listall(path,otstup=otstup+1)
        if os.path.isfile(path):
            print("file",'---'*otstup,f'{item}')

listall(main,0)  