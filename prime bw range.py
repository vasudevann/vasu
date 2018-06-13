m3 = int(input())
n3 = int(input())

for num in range(m3,n3+1):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
