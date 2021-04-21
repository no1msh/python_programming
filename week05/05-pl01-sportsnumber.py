sports = ["축구", "야구", "농구", "배구"]
num = [11, 9, 5, 6]
print(sports)
print(num)

for i in range(len(sports)):
    print("%s: %d명" % (sports[i], num[i]), end=" ")
print()
print()

snum = [sports, num]
print(snum)

for _ in range(len(sports)):
    print("%s: %d명" % (snum[0][_], snum[1][_]), end=" ")
print()
print()

liscom = [[sports[i], num[i]] for i in range(len(sports))]
print(liscom)

for _ in range(len(liscom)):
    print("%s: %d명" % (liscom[_][0], liscom[_][1]), end=" ")
