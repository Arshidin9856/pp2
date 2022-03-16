import os   
main=os.getcwd()
def listdir(MY_DIR, otstup):
    for item in os.listdir(MY_DIR):
        path=os.path.join(MY_DIR,item)
        if os.path.isdir(path):
            print('Dir','---'*otstup,f'{item}')
            listdir(path,otstup=otstup+1)
listdir(main,0)