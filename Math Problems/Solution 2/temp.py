dict = {}
errCount = {}
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
        dict[hostVal] = [str]
        errCount[hostVal+str] = 1
    else:
        if str not in dict[hostVal]:
            dict[hostVal].append(str)
            errCount[hostVal+str] = 1
        else:
            errCount[hostVal+str] += 1

def organizing():

def display():
    for key, value in dict.items():
    	print (key)
    	print ("-------------------")
    	for i in value:
    		print(i)
