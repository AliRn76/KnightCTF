def f(t):
    c = list(t)
    x = len(c) - 1

    for i in range(len(c)):
        value = c[-1]
        c.pop()
        c.insert(x - i, value)
    else:
        y = ''.join(i for i in c)
        print(f'{y = }')


if __name__ == "__main__":
    f('CFb5cp0rm1gK{1r4nT_m4}6')

    # flag = KCTF{b451c_pr06r4mm1ng}
