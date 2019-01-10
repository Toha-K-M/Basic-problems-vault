str = "Mr John Smith   "

str = list(str)
str = str[::-1]
flag = 0
for i in range(0,len(str)):
    if str[i]!=" ":
        flag = 1
    if flag is 1:
        if str[i] is " ":
            str[i] = '%20'
# reverse kore entry korlei hbe
str = ''.join(str[::-1])
print(str)