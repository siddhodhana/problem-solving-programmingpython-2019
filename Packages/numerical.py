#function to check if number is prime
def isprime(n):
    f=True
    for i in range(2,n//2):
        if n%i==0:
            f=False
    return f
#isprime(n)
#function to determine number of prime factors
def numberprimeFactors(n):
    if isprime(n):
        return 1
    count=0
    for i in range(2,n//2+1):
        if isprime(i) and n%i==0:
            count+=1
    return count
 
#numberprimeFactor()
            