Num=121

temp=121

rev=0

while temp !=0:
	
         rev=(rev*10)+(temp%10)
	
         temp=temp//10

if Num==rev:
	 
          print("yes")

else:
	 
          print("no")
