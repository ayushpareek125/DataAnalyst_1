import time

lst=list (range(1_000_000))
start=time.time()
[x*2 for x in lst]
print(time.time() - start)