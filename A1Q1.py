#  List the prime numbers up to 1000
def isprime(N):
    if N < 2: return False
    for n in range(2,N-1):
        if (N % n) == 0: return False
        if n >= N//n: break
    return True

p = list()
for x in range(1000):
    if isprime(x) == True:
        p.append(x)
print(p)


