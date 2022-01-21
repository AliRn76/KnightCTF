lower_keys = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
upper_keys = 'QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
number_keys = '1234567890'
symbol_keys = '!@#$%^&*()_+=-'

lower_codes = '1450 1456 1438 1451 1453 1458 1454 1442 1448 1449 1428 1430 1434 1452 1437 1439 1440 1441 1443 1444 1445 1396 1376 1459 1457 1436 1455 1435 1447 1446 1381 1383 1384 '
upper_codes = '1418 1424 1406 1419 1421 1426 1422 1410 1416 1417 1460 1462 1461 1402 1420 1405 1407 1408 1409 1411 1412 1413 1395 1371 1427 1425 1404 1423 1403 1415 1414 1397 1399 1400 '
number_codes = '1386 1387 1388 1389 1390 1391 1392 1393 1394 1385 '
symbol_codes = '1370 1401 1372 1373 1374 1431 1375 1379 1377 1378 1432 1380 1398 1382 '

encrypted_flag = ['1412', '1404', '1421', '1407', '1460', '1452', '1386', '1414', '1449', '1445', '1388', '1432', '1388',
                  '1415', '1436', '1385', '1405', '1388', '1451', '1432', '1386', '1388', '1388', '1392', '1462']

all_keys = list(lower_keys + upper_keys + number_keys + symbol_keys)

all_codes_str = lower_codes + upper_codes + number_codes + symbol_codes
all_codes = all_codes_str.split(' ')
all_codes = all_codes[:-1]

flag = []

for i in encrypted_flag:
    for j in all_codes:
        if i == j:
            index = all_codes.index(i)
            flag.append(all_keys[index])
            break
    else:
        flag.append('#')

flag_str = ''.join(i for i in flag)
print(flag_str)
# KCTF{s1Mpl3_3Nc0D3r_1337}
