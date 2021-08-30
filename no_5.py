a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
d=[]
for x in a:
        if x in a :
            c.append(x)
            if x not in d :
                d.append(x)
            else:
                pass
        else:
            pass

print('common numbers are ',d)
