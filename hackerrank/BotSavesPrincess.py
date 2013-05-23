
def displayPathtoPrincess(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                m = [i, j]
            elif grid[i][j] == 'p':
                p = [i, j]

    dX = p[1] - m[1]
    dY = p[0] - m[0]

    while dX > 0:
        print "RIGHT"
        dX -= 1
    while dX < 0:
        print "LEFT"
        dX += 1
    while dY > 0:
        print "DOWN"
        dY -= 1
    while dY < 0:
        print "UP"
        dY += 1



N = int(raw_input())
grid = []
for i in range(N):
    grid.append(list(raw_input()))

displayPathtoPrincess(N, grid)
