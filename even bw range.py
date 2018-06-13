m1=int(input())
n1=int(input())
evens = [str(x) for x in range(m1+1,n1) if x%2 == 0]
odds = [str(x) for x in range(m1+1,n1) if x%2 == 1]
print("\t" + "\t".join(evens))
