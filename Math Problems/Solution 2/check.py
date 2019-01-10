dict = {}
def host(line):
    words = line.split()
    for i in range(len(words)):
        if words[i] in ('Consumer','Producer'):
            return words[i+1]

def checking(line):
    hostVal = host(line)
    firstPor,secondPor = line.split('[ERROR]')
    str = '[ERROR]'+secondPor
    if hostVal not in dict:
        #if key not in dict
        dict[hostVal] = [[1,str]]
    else:
        #if key and value already in dict
        for i in dict[hostVal]:
            if str in i:
                i[0] += 1
                break
        else:
            #if key in dict but not value
            dict[hostVal].append([1,str])

def display():
    for key in dict:
        dict[key].sort(reverse=True)
        print(key)
        for value in dict[key]:
            print(value[0], ' - ',value[1])
