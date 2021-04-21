# for문으로 리스트 생성
a = []
for i in range(10);
    a.append(i)
print(a)

# 컴프리헨션으로 리스트 생성
seq = [i for i in range(10)]
print(seq)

# for 문으로 리스트 생성
s= []
for i in range(10):
    if i%2 == 1;
        s.append(i**2)
print(s)

# 컴프리헨션으로 리스트 생성
squares = [i**2 for i in range(10) if i%2 == 1]

# 컴프리헨션에선 콜론이 없다는 걸 주의 하자.