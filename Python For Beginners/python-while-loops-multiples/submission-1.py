i = 10
j = 0

while i < 100:
    j = 0
    while j < 10:
        if (i % 10) == j:
            print( i + j)
        j += 1
               
    i += 10
