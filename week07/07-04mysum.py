def mysum(x, y=0):  # 인자가 2개
    """두 수의  합 반환 함수"""
    return x + y  # 두인자의 합으로 반환


hap = mysum(5)  # y는 기본값이 0으로 인자가 하나만 입력 되었으므로 x는 5로 y는 디폴트 값인 0으로 들어갔다.
print(hap)

hap = mysum(5, 10)
print(hap)
