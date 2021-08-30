import sys

user=input('enter the number to check prime number :')
user = int(user)
def prime(user):
    for x in range(2,user-1):
        if user%x==0:
            print(f'{user} is not a prime number')
            sys.exit()
        elif user%x !=0:
            pass
    
    print(f'{user} is a prime number')
  
prime(user)
sys.exit()



