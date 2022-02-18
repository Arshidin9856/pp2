prime_list=list()
def filter_prime(l):
    for i in range(len(l)):
        def isprime(i):
            for n in range(2,int(i**1/2)+1):
                if i%n==0:
                    return False
            return True
        
        if isprime(i) and i>=2:
            
            prime_list.append(l[i])
filter_prime(input().split())
print (prime_list)