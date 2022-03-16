from string import ascii_uppercase
import os
for i in ascii_uppercase:
    
    f= open(f"{i}.txt","x")
    f.close()

    # os.remove(f"{i}.txt")
