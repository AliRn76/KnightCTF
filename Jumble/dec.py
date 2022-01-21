def f(t):
    c = list(t)
    # c = c[:-1]
    x = len(c) - 1

    for i in range(len(c)):
        value = c[-1]
        c.pop()
        c.insert(x - i, value)
    else:
        y = ''.join(i for i in c)
        print(f'{y = }')


if __name__ == "__main__":
    # flag = open("enc_flag", "r").read()
    f('CFb5cp0rm1gK{1r4nT_m4}6')

    # flag = S0NURnt5MHVfZzB0X20zfQ==  --->  KCTF{y0u_g0t_m3}
