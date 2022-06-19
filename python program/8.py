def my_fact(num):
    if num ==1:
        return 1
    else:

        fact = num * my_fact(num -1)
        return fact

n = 6
ans = my_fact(n)
print(ans)
