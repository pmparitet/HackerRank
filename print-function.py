if __name__ == '__main__':
    n = int(input('Введите число: '))

for i in range(1, n + 1):
    print(i, end='')


# Код автора
#
# print(*range(1, int(input()) + 1), sep="")
# или
# list(map(lambda x:print(x + 1, end=''), range(int(input()))))
