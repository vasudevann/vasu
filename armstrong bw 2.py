lower1 = int(input())
upper1 = int(input())
for numss in range(lower1, upper1):
   order = len(str(numss))
   sum = 0
   temp = numss
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if numss == sum:
       print(numss)
