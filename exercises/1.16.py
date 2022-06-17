#Write a program to print the cube of all numbers from 1 to a given number.

def cube(x):
    return x * x * x
n = int(input(" Enter the number : "))
cube1 = cube(n)
print("The Cube of {0}  = {1}".format(n, cube1))
