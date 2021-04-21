day1 = ("monday", "tuesday", "wednesday")
day2 = ("thursday", "friday", "saturday")
# ('sunday')로 하면 튜플이 아니고 문자열
day3 = ("sunday",)  # 튜플 선언을 위해 항목이 1개인 경우엔 끝에 ,를 붙여줌

day = day1 + day2 + day3
print(type(day))
print(day)

day = day1 + day2 + day3 * 3
print(day)