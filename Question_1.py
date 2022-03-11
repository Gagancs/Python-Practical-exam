"""

Write a function that finds the sum of the

a) first n odd terms

b) first n even terms

c) 1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term
"""

def even_sum(n):
    cnt = 2
    sum = 0
    i = 1
    while i <= n:
        sum += cnt
        cnt += 2
        i = i + 1
    return sum

def odd_sum(n):
    cnt = 1
    sum = 0
    i = 1
    while i <= n:
        sum += cnt
        cnt += 2
        i = i + 1
    return sum

def findSum(num):
    big_1 = 0
    smaller_1 = 0
    x = 1
    cur = 0
    ans = 0
    while (num > 0):
        inc = min(x, num)
        num -= inc
        if (cur == 0):
            ans = ans + odd_sum(big_1 + inc) - odd_sum(big_1)
            big_1 += inc
        else:
            ans = ans + even_sum(smaller_1 + inc) - even_sum(smaller_1)
            smaller_1 += inc
        x *= 2
        cur ^= 1
    return(ans)


n = int(input("Enter the value of N -_- : "))
print("sum of first ", n, "even number is: ", even_sum(n))
print("sum of first ", n, "odd number is: ", odd_sum(n))
print(findSum(n))