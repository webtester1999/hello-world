num = int(input('enter the number :'))
list = []
for x in range(100):
    if x%num == 0 :
        list.append(x)
    else:
        pass
print('list of all the divisors of  ',num, ' is ', list)
