if __name__ == '__main__':
    N = int(input())

# в список l записываем результат выполнения полученных команд
l = []

for _ in range(N):

    # получаем инструкцию, "split" Разбивает строку на части, используя разделитель,
    # и возвращает эти части списком
    s = input().split()

    # из полученного списка берем команду которую передают
    cmd = s[0]

    # берем второй элемент с аргументами
    args = s[1:]

    # если передана команда отличная от "print", то склеиваем полученную строку в команду
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l." + cmd)
    else:
        print(l)


# Код автора
#
# решение через if / elif
# при переборе полученной строки выполнять соответствующую команду
#
# arr = []
# for i in range(int(input())):
#     s = input().split()
#     for i in range(1, len(s)):
#         s[i] = int(s[i])
#
#     if s[0] == "append":
#         arr.append(s[1])
#     elif s[0] == "extend":
#         arr.extend(s[1:])
#     elif s[0] == "insert":
#         arr.insert(s[1], s[2])
#     elif s[0] == "remove":
#         arr.remove(s[1])
#     elif s[0] == "pop":
#         arr.pop()
#     elif s[0] == "index":
#         print
#         arr.index(s[1])
#     elif s[0] == "count":
#         print
#         arr.count(s[1])
#     elif s[0] == "sort":
#         arr.sort()
#     elif s[0] == "reverse":
#         arr.reverse()
#     elif s[0] == "print":
#         print
#         arr
