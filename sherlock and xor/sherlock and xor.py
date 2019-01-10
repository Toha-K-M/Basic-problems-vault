
T = input()
c = ''
while(T):
    n = input()
    ar = [0] * n
    counter = 0
    for x in range(0, n):
        num = input()
        ar[x] = num
    for y in range(0, n):
            ####
        if y != n-1:
            if (1 <= ar[y] < ar[y+1] <=n):
                q = ar[y]
                w = ar[y+1]
                c = ''
                while (q or w):
                    if (q & 1 != w & 1):
                        c += '1'
                    else:
                        c += '0'
                    q >>= 1
                    w >>= 1
            if c != '' and (int(c[::-1],2) % 2 != 0):
                counter += 1
        ####
        elif y == n - 1:
            if (1 <= ar[0] < ar[y] <= n):
                q = ar[0]
                w = ar[y]
                c = ''
                while (q or w):
                    if (q & 1 != w & 1):
                        c += '1'
                    else:
                        c += '0'
                    q >>= 1
                    w >>= 1
            if c != '' and (int(c[::-1], 2) % 2 != 0):
                counter += 1
        else:
            pass
    print counter
    T -= 1



#c = c[::-1]
#print int(c,2)




