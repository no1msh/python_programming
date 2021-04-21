time = input('시각 정보(16:30:15) 입력 >> ')
print(time)
hours, mins, secs = time.split(':')
print(hours+'시', mins+'분', secs+'초')
# +로 변수와 문자열을 이으면 공백이 생기지 않는다. ','를 사용하면 공백이 생김.
