w = int(input())
e = int(input())

for num in range(w,e+1):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
