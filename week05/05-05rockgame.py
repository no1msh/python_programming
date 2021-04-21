rsp = ["가위", "바위", "보"]
for i in range(len(rsp)):
    print(rsp[i], end=" ")
print()

from random import choice

print("컴퓨터 가위 바위 보 5개")
for i in range(5):
    print(choice(rsp))