def fibna(num = int(input('total number'))):
    
    i=[1,1]
    if num==1:
        print([1])
    elif num==2:
        print([1,1])
    else:
        for x in range(num):
            i.append(i[-1]+i[-2])
    print(i)
fibna()
        
