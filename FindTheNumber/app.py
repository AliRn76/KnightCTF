def g_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + g_sum(n-1)


print(g_sum(25))

# flag = KCTF{1.9999999701976776}
