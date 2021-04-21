str = 'Hello python!'  # str에 문자열 값 입력
n = len(str)  # 변수 n에 str 문자열의 길이 저장
print('문자열', str, '길이', n)
print('첫 문자', str[0], str[-n])  # 두개 모두 첫문자 출력
print('가운데 문자', str[n//2], str[-n//2])  # 두개 모두 가운데 문자 출력
print('마지막 문자', str[n-1], str[-1])  # 두개 모두 마지막 문자 출력
