def c(n):
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                yield (i,j,k)

print(list(c(5)))