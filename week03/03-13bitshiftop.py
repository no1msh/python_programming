num = int(input('이동 연산 num << cnt를 수행할 정수 num 입력 ? '))
cnt = int(input('이동 연산 num << cnt를 수행할 정수 cnt 입력 ? '))

print('{0:032b} {0:8d} :num'.format(num))
print('{2:032b} {2:8d} :{0} << {1}'.format(num, cnt, num << cnt))
print('{2:032b} {2:8d} :{0} * 2 **{1}'.format(num, cnt, num * 2**cnt))
# 왼쪽으로 3칸 비트 이동의 결과 값은 2의 3제곱 , 즉 8을 곱한 값과 같다.
