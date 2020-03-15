
# Insert the input value into a variable
p = int(input("Please enter a positive Integer:"))
b = 2


while p > 1:
    if p % b == 0:
       print(p)
       print (p / b)
       break
    else: 
        p =  (p * 3) + 1 
        print(p)
        print (p / b)




