menu = ("주문종료", "올인원팩", "투게더팩", "트리오팩", "패밀리팩")
price = (0, 6000, 7000, 8000, 10000)
total = 0
msg = "주문할 콤보 번호와 수량을 계속 입력하세요!"
while True:
    print(msg)

    for _ in range(len(menu)):
        print("\t%d. %s %5d원" % (_, menu[_], price[_]))

    answer = input(">>")

    if answer.count(" ") > 0:
        combo_num, combo_count = answer.split()

    if answer == "0":
        print("주문종료".center(20, "*"))
        print("총 주문 가격 %d 원" % total)
        print("주문을 마치겠습니다.")
        print(" 안녕! ".center(20, "="))
        break

    combo_num = int(combo_num)
    combo_count = int(combo_count)

    total += price[combo_num] * combo_count
    print("%s, %d개 주문" % (menu[combo_num], combo_count))
    print("%s 주문 가격 %d, 총 가격\n%d\n" % (menu[combo_num], price[combo_num], total))
