def remove_digits(num, m):
    count = 0
    n = len(num)
    while count < m:
        i = 0
        while i < len(num) - 1:
            if num[i] < num[i + 1]:
                num.pop(i)
                count += 1
                break
            elif i + 1 == len(num) - 1 and num[i] >= num[i + 1]:
                num.pop(i + 1)
                count += 1
                break
            i += 1
    return num


t = int(input())

for _ in range(t):
    num_str, m = input().split()
    m = int(m)
    num = [int(d) for d in num_str]
    result = remove_digits(num, m)
    print(*result, sep="")