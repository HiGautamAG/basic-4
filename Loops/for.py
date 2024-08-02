# for loops in python are used to iterate over a sequence (list, tuple, string) or other iterable objects.

veg = ["potato", "tomato", "onion", "carrot"]

for i in veg:
   print(i)
   
   


# for tupple 

tup = (1, 2, 3, 4, 5)

for i in tup:
    print(i)
    
    
    
# for string

string = "Gautam Ansh"

for i in string:
    print((i))
    
    
str = "GODZILLA THE KING OF MONSTER"

for char in str:
    print(char)
    
else:
    print("No error")
    # else block will execute when for loop is completed without any error.
    
    
 #question   
    
LIST =[1, 4, 16, 25, 36, 49, 64, 81, 100]

for i in LIST:
    print(i)
    
    
    
    
    
list =( 1, 4, 16, 25, 36, 49, 64, 81, 100) 
y = 16

idx =0
for an in list:
    if (an == y):
        print("Element found at index", idx)
    idx += 1   