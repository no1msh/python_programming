# 2. 킬로미터 단위로 거리를 입력받아 마일(mile) 단위로 변환해 출력하는 프로그램을 작성하시오.
# 1마일은 1.61km

speed_km = float(input("차의 속도를 입력(km): "))
speed_mile = float(speed_km/1.61)

print(speed_km, '(km)은 ', speed_mile, '마일(miles)이다.')
