# Чистый код
#
# n = int(input())
# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")


# !/bin/python3

N = int(input())

if N % 2 != 0:
    print('Weird')
else:
    if 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20:
        print('Weird')
    else:
        print('Not Weird')
