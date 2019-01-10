str = "tata"

# table
table = [0]*128 #assume ascii

for i in str:
    table[ord(i)] = table[ord(i)]+1

c = 0
for i in table:
    if(i):
        if i % 2 != 0:
            if c > 1:
                break
            else:
                c = c + 1

if c > 1:
    print("no")
else:
    print("yes")

a = "taat"
if (a != a[::-1]):
    print("not palindrome")
else:
    print("palindrome")