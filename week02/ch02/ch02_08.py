# 8. 네 자릿수 정수를 입력받은 후 그정수를 역순으로 출력하는 프로그램을 작성하시오.

integer = int(input('네 자릿수 정수 입력: '))

integer1000 = integer//1000
integer100 = (integer-integer1000*1000)//100
integer10 = (integer-integer1000*1000-integer100*100)//10
integer1 = (integer-integer1000*1000-integer100*100-integer10*10)

print(integer1, integer10, integer100, integer1000, sep="")
