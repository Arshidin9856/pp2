"""
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""
from math import sqrt
import time 

n=int(input())
t=int(input())
time.sleep(t/1000)
print(f"Square root of {n} after {t} miliseconds is {sqrt(n)}")