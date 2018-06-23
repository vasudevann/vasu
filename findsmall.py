# your code goes here
n=int(input())
m=(input())
list=m.split(" ")
q=int(list[0])
for i in range (1,n):
	if(q>int(list[i])):
		q=int(list[i])
print(q)		

