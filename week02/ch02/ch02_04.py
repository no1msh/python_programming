# 4. 다음 조건을 참고해 지구를 원이라고 보고 원의 돌레를 계산해
# 실제와의 차이를 알아보는 프로그램을 작성하시오.
# 지구의 둘레는 4만 120km , 반지름은 6378.1km
# 원둘레 공식 : 2 X 3.141592 X r(반지름)

earth_round_real = 40120
earth_r = 6378.1
earth_round = 2*3.141592*earth_r

print('알려진 지구 둘레: ', earth_round_real)
print('지구와 같은 원 둘레: ', earth_round)
print('차이: ', earth_round_real-earth_round, '(km)')
