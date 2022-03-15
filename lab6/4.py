import os
#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path
path=input("Choose path in LAB_WORKS: ")
print(f'Path existense: {os.access(os.path.join(os.getcwd(),path),os.F_OK)}')
print(f'Path readability: {os.access(os.path.join(os.getcwd(),path),os.R_OK)}')
print(f'Path writability: {os.access(os.path.join(os.getcwd(),path),os.W_OK)}')
print(f'Path executability: {os.access(os.path.join(os.getcwd(),path),os.X_OK)}')
