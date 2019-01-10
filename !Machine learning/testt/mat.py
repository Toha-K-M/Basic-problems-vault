def dada(x):
    def add(x):
        x = x+2
        return x

    y = add(x)
    y += 2
    return y
