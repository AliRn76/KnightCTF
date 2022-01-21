import math


number1 = 21525625
number2 = 30135875

gcd = math.gcd(number1, number2)

gcd_list = list(str(gcd))
sum_gcd = 0

for i in gcd_list:
    sum_gcd += int(i)

print(f'{sum_gcd = }')
final = 1234 * sum_gcd
print(f'{final = }')

# flag = KCTF{24680}