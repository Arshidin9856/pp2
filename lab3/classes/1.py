
class Myclass:
    def __init__(self,string):
        self.string=string
    def print(self):
        print(self.string.upper())
c=input()
p=Myclass(c)
p.print()
