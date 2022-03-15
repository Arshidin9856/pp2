# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
my_path=input("Choose path: ")
if os.path.exists(my_path):
    print(f'Path existense: {os.access(my_path,os.F_OK)}')
    print(f'Path readability: {os.access(my_path,os.R_OK)}')
    print(f'Path writability: {os.access(my_path,os.W_OK)}')
    print(f'Path executability: {os.access(my_path,os.X_OK)}')
    os.remove(my_path)
    print("Path removed")