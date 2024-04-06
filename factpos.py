def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def nth_prime(pos):
    count = 0
    n=2
    while True:
        if prime(n):
            count += 1
            if count == pos:
                return n
        n+=1

n=int(input("Enter the position:"))
print("The prime number at position",n,"is:",nth_prime(n))
