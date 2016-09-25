import gmpy2
from math import sqrt

primes = set()
n = 2
for i in range(10000):
    n = gmpy2.next_prime(n)
    primes.add(n)

while 1:
    p, q = map(int, input("Type two prime numbers : ").split(' '))
    if p in primes and q in primes:
        break
    else:
        print("Please type again!")

n = p * q
funcn = (p - 1) * (q - 1)

while 1:
    e = int(input("Type value of 'e' : "))
    if int(gmpy2.gcd(e, funcn)) == 1:
        break
    else:
        print("Please type again!")

d = gmpy2.invert(e, funcn)

print("Your public key is{", e,',',n,'}')
print("Your private key is{", d,',',n,'}')

print("Choose option 1)Encryption 2)Decryption")
choice = input()

text = int(input("Type your text : "))

if choice == '1':
	c = gmpy2.powmod(text,e,n)
	print("Cyphered text is", c) 

else:
	p = gmpy2.powmod(text,d,n)
	print("Plaintext is", p)
