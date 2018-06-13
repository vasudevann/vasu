m=int(input())
n=int(input())
evens = [str(x) for x in range(m+1,n) if x%2 == 0]
odds = [str(x) for x in range(m+1,n) if x%2 == 1]
print("\t" + "\t".join(evens))
