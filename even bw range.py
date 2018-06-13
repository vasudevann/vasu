m2=int(input())
n2=int(input())
evens = [str(x) for x in range(m2+1,n2) if x%2 == 0]
odds = [str(x) for x in range(m2+1,n2) if x%2 == 1]
print("\t" + "\t".join(evens))
