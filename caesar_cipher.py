from string import ascii_letters
n = int(input("1=> Encryption 2=> Decryption : "))
s = input("Type string for  : ")
key = int(input("Type key value : "))
outval = ascii_letters[key:] + ascii_letters[:key]
if n == 1:
    print("Answer string is", s.translate(str.maketrans(ascii_letters, outval)))
else:
    print("Answer string is", s.translate(str.maketrans(outval, ascii_letters)))
