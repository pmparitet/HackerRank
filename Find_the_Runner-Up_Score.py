if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]


q = max(arr)

while max(arr) == q:
    arr.remove(max(arr))

print(max(arr))
