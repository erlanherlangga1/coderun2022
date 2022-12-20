import sys
import tracemalloc

tracemalloc.start()

def solution(n, m):
  angka=[]
  if n<=1000000000 and m<=1000000000 and n>=1 and m>=1:
    if n>m:
        for i in range(n):
          b=i+1
          if n%b==0 and m%b==0:
            angka.append(b)
    else:    
        for j in range(m):
          b=j+1
          if m%b==0 and n%b==0:
            angka.append(b)
  else:
    sys.exit("Invalid Input")

  print (len(angka))

solution(8,12)
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno"):
    print(stat)