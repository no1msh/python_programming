lst = [10, 30, 40, 50]
lst[:3] = 100, 100, 100, 100, 100
print(lst)

# Q1. 왜 [:3]이면 3번째 항목 까지 값이 저장 되어야 할 것 같은데 그 이상 저장이 가능한지?
# Q2. 왜 lst[:3] = 100 이 3번째 원소 까지 100을 대입해라 즉 100을 3개 대입해라라는 뜻이 아닌지?