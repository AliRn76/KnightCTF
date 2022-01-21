import os
from subprocess import Popen, PIPE

images = os.listdir('images/')
collected = []
images.sort()

for i in images:
    sp = Popen(['zbarimg', 'images/{}'.format(str(i))], stdout=PIPE, stderr=PIPE)
    sp.wait()
    msg = str(sp.communicate()[0][:-1])
    collected .append(msg[8:])

collected.reverse()
collected_str = ''.join(i for i in collected)
collected_ord = [ord(i) for i in collected]
final_ord = []

# alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet = list('abcdefghijklmnopqrstuvwxyz')



# TRY 2

final = []
for v in collected:
    if v in ['{', '}', '_']:
        final.append(v)
    else:
        i = alphabet.index(v.lower())
        final.append(alphabet[i - 13])
print(''.join(i for i in final))


## TRY 1
# for i, v in enumerate(collected_ord):
#     n = i+1
#     # print(i, n, (n % 5), n != 1 and not bool(n % 5), chr(v))
#
#     # if n != 1 and not bool(n % 5):
#     if v in [123, 125]:
#         print(chr(v), v, ' ---------> ', v, chr(v))
#         print('')
#         final_ord.append(v)
#     # elif (n % 5) in [1, 2, 4]:
#     elif v >= 80:
#         print(chr(v), v, ' --(-13)--> ', v-13, chr(v-13))
#         final_ord.append(v - 13)
#     else:
#         print(chr(v), v, ' --(+13)--> ', v+13, chr(v+13))
#         final_ord.append(v + 13)
#
# final_str = ''.join(chr(i) for i in final_ord)
# print(collected_str)
# print(final_str)
# print(ord('X'), ord('P'), ord('G'), ord('S'), ord('{'), ord('}'))
# print(ord('K'), ord('C'), ord('T'), ord('F'), ord('{'), ord('}'))
