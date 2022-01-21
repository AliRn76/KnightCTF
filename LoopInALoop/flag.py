

flag = input()
flag = list(flag)
for i in range(len(flag)):
    j = i
    while j < len(flag) - 1:
        flag[j], flag[j+1] = flag[j+1], flag[j]
        j += 1
    y = ''.join(i for i in flag)
    print(f'{y = }')
