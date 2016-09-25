import gmpy2

def primitive(a, b):
    s = set()
    for i in range(1, b):
        tmp = (a**i) % b
        if tmp in s:
            return 0
        else:
            s.add(tmp)
    return 1
primes = set()
n = 2
for i in range(10000):
    n = gmpy2.next_prime(n)
    primes.add(n)

while 1:
    q = int(input("Type a prime number : "))
    if q in primes:
        break
    else:
        print("Type number again")

while 1:
    a = int(input("Type the primitive root of prime number : "))
    if primitive(a,q):
    	break
    else:
        print("Type number again")

xa = int(input("Type A's private key : "))    	
xb = int(input("Type B's private key : "))

ya = int(gmpy2.powmod(a, xa, q))
yb = int(gmpy2.powmod(a, xb, q))

print("A's public key ",ya)
print("B's public key ",yb)
