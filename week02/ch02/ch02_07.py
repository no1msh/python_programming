# 7. 다음에서 설명하는 float.fromhex(str)를 이해하고 두 16진수 실수를 입력받아
# 사칙연산을 수행하는 프로그램을 작성하시오.
# 실수 float에 속한 함수 (정확한 명칭은 메소드라고 함)
# float.fromhex(str)는 16진수 형태의 문자열 str을 실수로 변환하는 함수
# 즉 float.from('f')는 15, float.from('e.1')은 14.0625

hexnum1 = input('첫 번쨰 16진수 실수 입력 ')
hexnum2 = input('두 번째 16진수 실수 입력 ')
hexnum1 = float.fromhex(hexnum1)
hexnum2 = float.fromhex(hexnum2)

print('실수1: ', hexnum1, '실수2: ', hexnum2)

print('합: ', hexnum1+hexnum2)
print('차: ', hexnum1-hexnum2)
print('곱하기: ', hexnum1*hexnum2)
print('나누기: ', hexnum1 / hexnum2)
