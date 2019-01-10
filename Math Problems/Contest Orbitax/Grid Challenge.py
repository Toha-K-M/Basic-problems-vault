t = int(input())

for t_itr in range(t):
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))
    l = len(grid[0])

    def isSorted(x):
        return all(x[i] <= x[i + 1] for i in range(len(x) - 1))

    for i in range(l):
        x = []
        for j in range(len(grid)):
            x.append(grid[j][i])
        if not isSorted(x):
            return 'NO'

    return 'YES'

print(gridChallenge(grid))