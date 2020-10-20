print('1 부터 n 까지 정수의 합')
n = int(input('n 값 입력 : '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1 부터 {n} 까지 합은 {sum} 입니다.')
