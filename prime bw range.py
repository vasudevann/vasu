w = int(input())
e = int(input())

for tem in range(w,e+1):
   
   if tem > 1:
       for i in range(2,tem):
           if (tem % i) == 0:
               break
       else:
           print(tem)
