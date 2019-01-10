str = "toha"

def isUnique(str):
    if len(str) > 128:
        return False
    bool = [0]*128
    for i in str:
        val = ord(i)
        if(bool[val]):
            return False
        bool[val] = 1
print(isUnique(str))### here none is no duplicate