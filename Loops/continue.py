#continue statement in while loop   



i = 0 
while i < 10:
    if(i == 5):
        i += 1
        continue # skip the current iteration
    print(i)
    i+=1


i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1