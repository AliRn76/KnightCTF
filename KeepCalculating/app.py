
x = 1
y = 2
answer = 0

while x <= 666:
    answer += (x * y) + int(str(x) + str(y))
    x += 1
    y += 2
# print(x)

print(answer)
