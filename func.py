n = 6
lim = n + ((n - 2) / 2)

def tri(n):
    return int((n * (n + 1)) / 2)

def cell(i):
    t = tri(i)
    if i <= n:
        return t
    elif i <= lim:
        return t - (3 * tri(i - n))

for i in range (1, (3 * n - 1)):
    if i <= lim:
        print(cell(i))
    else:
        print(cell(lim - ((i - 1) % lim)))
