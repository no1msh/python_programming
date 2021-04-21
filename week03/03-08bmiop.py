h, w = input('당신의 키 (cm) 와 몸무게 (kg)는? >> ').split()
height = float(h)
weight = float(w)
bmi = weight / (height/100)**2
print('키:%6.1f(cm), 몸무게:%5.1f(kg), BMI:%5.1f' % (height, weight, bmi))
# 여러 항목 출력하는 방법  ↑  %로 형식 지정을 했으면 뒤에 % 쓰고 괄호로 묶어주기
print('{} {}'.format('고도 비만', 40 <= bmi))
print('{} {}'.format('중등도 비만', 35 <= bmi < 40))
print('{} {}'.format('비만', 30 <= bmi < 35))
print('{} {}'.format('과체중', 25 <= bmi < 30))
print('{} {}'.format('정상', 18.5 <= bmi < 25))
print('{} {}'.format('저체중', bmi < 18.5))
