intejer1 = int(input("정수 입력 >> "))
exp1 = int(input("2의 지수승 입력 >> "))

print("\n{} << {}, 결과: {}".format(intejer1, exp1, intejer1 << exp1))
print("{} * 2**{}, 결과: {}".format(intejer1, exp1, intejer1 * 2 ** exp1))
print("2진수(32비트): {:32b} 정수: {}".format(intejer1, intejer1))
print("2진수(32비트): {:32b} 정수: {} << {}".format(intejer1 << exp1, intejer1, exp1))
print("2진수(32비트): {:32b} 정수: {} * 2**{}".format(intejer1 * 2 ** exp1, intejer1, exp1))
