import numpy as np
# currently applicable for python2 only
key = np.arange(9).reshape((3, 3))
for i in range(3):
    s = raw_input()
    key[i] = [int(j) for j in s.split(' ')]

print("Your key is", key)
s = raw_input("Type string for encryption")
s += 'A' * (3 - len(s) % 3)

for i in range(0, len(s), 3):
    y = np.arange(3)
    y = [ord(j) + 1 - ord('A') for j in s[i:i + 3]]
    print("mul")
    ans = np.dot(key, y)
    print("ans", ans)
    tmp = [chr(max(0,(j%26-1))+ord('A')) for j in ans ]
    print(str(tmp))
