# 2진수는 8비트의 정보 표현으로 출력
# 8진수와 16진수는 2진수의 비트 표현에서 8진수와 16진수로 출력
mask = 0xFF  # & mask 를 통하여 음수의 내부비트 정보를 출력 할 수 있음.
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-7, -7 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-6, -6 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-5, -5 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-4, -4 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-3, -3 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-2, -2 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(-1, -1 & mask))
print("10진수: {0} 2진수: {1:08b} 8진수: {1:4o} 16진수: {1:2x} ".format(0, 0 & mask))
