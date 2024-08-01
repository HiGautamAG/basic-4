    
# break statement in while loop

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
    
    
   
nums = [1, 11, 21, 32, 41, 51, 61, 71, 81, 91]

x = 41

indx = 0
while indx < len(nums):
    if nums[indx] == x:
        print("Element found at index", indx)
        break
    else:
        print("finding...")
    indx += 1 