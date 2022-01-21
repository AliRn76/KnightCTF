
def square_sum(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)

    return sm


print(square_sum(25000))
