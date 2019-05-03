# Задача: посчитать среднее значение оценок, данные передаются в словаре "имя:оценка"
# query_name - имя, для поиска в словаре по ключу
# задание и вводные для проверки в "finding-the-percentage.pdf"
# 
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# находим имя=key в словаре и записываем в переменную
query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
