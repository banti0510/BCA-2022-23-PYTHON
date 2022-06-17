# Write a program to display only those numbers from a list that satisfy the following
conditions
 The number must be divisible by five
 If the number is greater than 150, then skip it and move to the next number
 If the number is greater than 500, then stop the loop

a = [12, 75, 150, 180, 145, 525, 50]
b = []
for i in a:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        b.append(i)
        
print(b)
