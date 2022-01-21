def f(t):
    c = list(t)
    for i in range(len(t)):
        # y = ''.join(i for i in c)
        # print(f'{y = }')
        for j in range(i, len(t) - 1):
            c[j], c[j+1] = c[j+1], c[j]
    return "".join(c)

if __name__ == "__main__":
    flag = open("custom_flag", "r").read()
    open("ciphertext", "w").write(f(flag))
