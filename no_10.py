import random

'''
list_a = []
list_b = []

for xa in range(10):
    Rnum= random.randrange(1,10)
    list_a.append(Rnum)
for xb in range(10):
    Rnum= random.randrange(1,10)
    list_b.append(Rnum)
    
print(list_a)
print(list_b)

c = []
d = []
for x in list_a:
    if x in list_b:
      c.append(x)  
      for n in c:
          if n not in d:
              d.append(n)
          else:
              pass
    else:
        pass
print(d)
'''

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]
print(result)
