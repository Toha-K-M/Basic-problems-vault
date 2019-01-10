from itertools import permutations

a = 'cbaabbb'

plist = permutations(a)
x = []
for perm in list(plist):
    if ''.join(perm) not in x:
        x.append((''.join(perm)))

print(len(x))