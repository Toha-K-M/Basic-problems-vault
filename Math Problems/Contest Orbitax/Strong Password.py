numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

flags = [0]*4
##
x="#HackerRank"
for i in x:
   if i in numbers:
       flags[0]=1
   elif i in lower_case:
       flags[1]=1
   elif i in upper_case:
       flags[2]=1
   elif i in special_characters:
       flags[3]=1
count = 0
for i in flags:
    if i is 0:
        count += 1

if len(x)+count >= 6:
    print(count)
else:
    print(6-len(x))