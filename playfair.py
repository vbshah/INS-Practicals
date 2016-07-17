choice = int(input("1) Encryption 2) Decryption : "))
key = input("Type key string : ")
done = [0] * 26
done[ord('j') - ord('a')] = 1
ls = [[''] * 5 for i in range(5)]
main_index = 0
data = {}
for i in key:
    if not done[ord(i) - ord('a')]:
        x = int(main_index / 5)
        y = main_index % 5
        ls[x][y] = i
        done[ord(i) - ord('a')] = 1
        main_index += 1
        data[i] = (x, y)
c = 0
while c < 26:
    if not done[c]:
        x = int(main_index / 5)
        y = main_index % 5
        ls[x][y] = chr(c + ord('a'))
        done[c] = 1
        main_index += 1
        data[chr(c + ord('a'))] = (x, y)
    c += 1
# ls=[input().split(' ') for i in range(5)]
s = input("Type the string for encryption or decryption : ").replace('j', 'i')
# arr=[s[i]+s[i+1] for i in range(0,len(s)-1,2)]
arr = []
i = 0
while i < len(s) - 1:
    a = s[i]
    b = s[i + 1]
    if a != b:
        arr.append(a + b)
        i += 2
    else:
        arr.append(a + 'z')
        i += 1
if i != len(s):
    arr.append(s[len(s) - 1] + 'z')
ans = []
if choice == 1:
    for i in arr:
        x1, y1 = data[i[0]]
        x2, y2 = data[i[1]]
        if x1 == x2:
            ans.append(ls[x1][(y1 + 1) % 5] +
                       ls[x2][(y2 + 1) % 5])
        elif y1 == y2:
            ans.append(ls[(x1 + 1) % 5][y1] +
                       ls[(x2 + 1) % 5][y2])
        else:
            ans.append(ls[x1][y2] + ls[x2][y1])
else:
    for i in arr:
        x1, y1 = data[i[0]]
        x2, y2 = data[i[1]]
        if x1 == x2:
            ans.append(ls[x1][(y1 - 1) % 5] +
                       ls[x2][(y2 - 1) % 5])
        elif y1 == y2:
            ans.append(ls[(x1 - 1) % 5][y1] +
                       ls[(x2 - 1) % 5][y2])
        else:
            ans.append(ls[x1][y2] + ls[x2][y1])

print("Answer string is", ''.join(ans))


# p l a y f
# i r b c d
# e g h k m
# n o q s t
# u v w x z
