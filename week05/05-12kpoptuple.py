singer = ("BTS", "볼빨간사춘기", "BTS", "블랙핑크", "태연")
song = ("작은 것들을 위한 시", "나만, 봄", "소우주", "Kill This Love", "사계")
print(singer)
print(song)

print(singer.count("BTS"))
print(singer.index("볼빨간사춘기"))
print(singer.index("BTS"))
print()  # 줄바꿈용

for _ in range(len(singer)):  # 단순 프린트 문만 반복하는 경우 변수는 무의미 하기에 _를 사용
    print("%s : %s" % (singer[_], song[_]))
