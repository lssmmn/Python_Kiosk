import os, time #내장 모듈인 os와 time 선언

# 'TERM' 환경변수가 없으면 'xterm-256color'로 설정 (터미널 색상 설정)
if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm-256color'

# 아트 및 메뉴 텍스트 불러오기 (외부 라이브러리로부터)
from console_art import login_art, main_art, menu_list_art, main_login_art, guest_login_art, time_charge_art, \
    menu_list_all, menu_list_set, menu_list_drink, menu_list_food, menu_list_option_food, menu_list_food_side, \
    paymentmeth_art, paymentmeth_fail, paymentmeth_cash_fail, paymentmeth_card_fail, paymentmeth_kakao_fail,  pay_complte_art_top, pay_complte_art_bottom, paymentmeth_art_kakao, \
    paymentmeth_art_card, paymentmeth_art_cash,cart_art_top

# 콘솔 화면을 지우는 함수 (운영체제에 따라 다르게 처리)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# 미리 등록된 사용자 데이터 (아이디, 비밀번호)
user_db = {
    '관리자': ['admin', '1q2q3e'],
    '수민': ['1103', '1103'],
    '진리': ['123', '123'],
    '연주': ['555', '555'],
    '재은': ['618', '618'],
    '명진': ['0806', '0806'],
    '왕신': ['5216', '5216']
}

# 로그인 함수
def login():
    clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
    print(login_art)
    print("     system : 아이디를 입력하세요.")
    user_id = input("     >>> ")
    print("     system : 비밀번호를 입력하세요.")
    password = input("     >>> ")

    for username, credentials in user_db.items(): # 등록된 데이터 딕셔너리를 키와 값으로 설정
        if credentials[0] == user_id and credentials[1] == password:  # 아이디와 비밀번호 확인
            clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
            print(f"     {'￣'*35}")
            print(f"     {username}님, 아이센스리그 PC방에 오신 것을 환영합니다! 즐거운 시간 되세요!")
            print(f"     {'￣'*35}")
            time.sleep(1)
            clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
            return True

    print("     system : 등록된 정보가 없습니다. 관리자에게 문의하세요.")
    input("     system : 다시 시도하려면 Enter 키를 누르세요.")
    return False

# 비회원 로그인 함수
def guest_login():
    clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
    print(guest_login_art)
    while True:
        print("     system : PC 번호 입력")
        pc_number = input("     >>> ").strip()
        if not pc_number.isdigit():  # 숫자가 아닌 입력값 처리
            print("     system : 숫자만 입력해주세요.")
            continue
        pc_num = int(pc_number)
        if 1 <= pc_num <= 50:  # PC 번호가 1~50 범위 내에 있는지 확인
            break
        else:
            print("     system : 올바른 번호를 입력해주세요 (1~50).")
    clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
    print(f"     {'￣'*35}")
    print(f"     PC 번호 {pc_num}번으로 접속하셨습니다! 즐거운 시간 되세요!")
    print(f"     {'￣'*35}")
    input("     system : 계속하려면 Enter 키를 누르세요.")
    clear_console()
    return True


# 요금 충전 화면을 관리하는 함수
def rate_plan():
    # 요금제와 그에 맞는 충전 시간을 딕셔너리로 정의
    rate_plan_db = {
        '1000': ['00:50'],
        '2000': ['01:30'],
        '3000': ['02:00'],
        '5000': ['03:30'],
        '10000': ['07:30'],
        '20000': ['14:30'],
        '30000': ['22:30'],
        '50000': ['37:00']
    }

    lst = ['돌아가기', '1000', '2000', '3000', '5000', '10000', '20000', '30000', '50000']  # 요금제 선택 목록

    while True:
        clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
        print(time_charge_art)  # 요금 충전 아트 출력
        print("     system : 충전할 요금을 선택해 주세요.")
        print("     번호 입력")

        user_input = input("     >>> ")

        if user_input == "0":
            print("     system : 이전화면으로 돌아갑니다.")
            clear_console()
            return main_screen()  # 돌아가기 시 메인 화면으로 이동

        try:
            idx = int(user_input)  # 사용자 입력값을 숫자로 변환
            charge_price = lst[idx]  # 선택된 요금제
        except (ValueError, IndexError):  # 유효하지 않은 입력값 처리
            print("     system : 잘못된 입력입니다. 다시 선택해주세요.")
            continue

        if charge_price in rate_plan_db:
            # 충전 금액이 유효하면 결제 함수 호출
            pay(charge_price)
            input("     system : 계속하려면 Enter 키를 누르세요.")
            return "to_main"
        else:

            print("     system : 해당 요금제가 없습니다.")
            continue

# 요금결제관리함수
def pay(charge_price):
    clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
    print(paymentmeth_art)  # 결제 아트 출력 (visual art을 보여줌)
    print("     지불할 금액은", charge_price,"원 입니다.")  # 사용자가 결제할 금액을 출력
    # 결제 방법을 리스트로 제공 (뒤로가기, 현금, 신용카드, 카카오페이)
    lst = ["뒤로가기", "현금", "신용카드", "카카오페이"]  # 결제 방법 목록
    try: # 결제 방법을 번호로 입력 받음
        print("     system : 결제방식을 입력하세요.")
        pay_way = int(input("     >>> "))  # 사용자로부터 결제 방법을 선택할 수 있도록 유도
    except ValueError:  # 입력값이 숫자가 아닐 경우 예외 처리
        print("     system : ❌ 숫자를 입력해 주세요.")     # 사용자에게 숫자 입력을 유도하는 메시지 출력
        return rate_plan()      # 잘못된 입력 시, 결제 화면을 다시 표시하기 위해 rate_plan 함수 호출
    if not 0 <= pay_way < len(lst):     # 선택한 결제 방법이 유효한지 확인
        # 번호가 0에서 len(lst)-1 범위 밖일 경우
        print("     system : ❌ 올바른 번호를 입력해 주세요.")  # 올바른 번호 입력을 요구하는 메시지 출력
        return pay(charge_price)  # 잘못된 입력 시, 결제 화면을 다시 표시하기 위해 rate_plan 함수 호출
    elif pay_way == 0:  # 뒤로가기 선택 시
        print("     system : 이전화면으로 돌아갑니다.")
        return rate_plan()  # 결제 진행하지 않음
    else:
        print("     system : 다시 입력하세요.")
    pay_way = lst[pay_way]  # 결제 방법 리스트에서 선택된 결제 방식

    # 현금결제
    if pay_way == "현금":
        while True:
            clear_console()
            # 사용자에게 현금을 입력하도록 요청
            print(paymentmeth_art_cash) #현금 결제 아트 출력
            print("     지불할 금액은",charge_price,"원 입니다.") #사용자가 결제할 금액을 출력
            print("     system : 현금을 넣어 주세요")
            money = int(input("     >>> "))  # 현금 금액 입력
            clear_console()
            if money == 0:
                # 사용자가 0원을 입력한 경우
                print(paymentmeth_cash_fail)  # 결제 실패 아트 출력
                print("     system : ❌ 결제가 취소되었습니다.")  # 금액이 부족하여 결제 취소 메시지 출력
                input("     system : 계속하려면 Enter 키를 누르세요.")
                return main()  # 결제 취소, False 반환
            elif int(charge_price) <= money:    # 입력한 금액이 결제 금액 이상인 경우
                # clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움
                change_money = money - int(charge_price)    # 거스름돈 계산
                print(pay_complte_art_top)      # 결제 완료 아트 출력
                print(" " * 9, charge_price, "원")   # 결제 금액 출력
                print(pay_complte_art_bottom)   # 결제 완료 아트 하단 출력
                print("     거스름돈 >>> ", change_money)     # 거스름돈 출력
                input("     system : 계속하려면 Enter 키를 누르세요.")
                return main()  # 결제 완료
            else:
                # 입력한 금액이 부족한 경우
                print(paymentmeth_cash_fail)  # 결제 실패 아트 출력
                print("     system : ❌ 금액이 부족합니다. 다시 시도해 주세요.")  # 부족한 금액에 대한 안내 메시지 출력
                input("     system : 계속하려면 Enter 키를 누르세요.")
                continue  # 다시 현금을 입력 받기 위해 반복

    # 신용카드결제
    elif pay_way == "신용카드":
        # 카드 결제 아트 출력
        clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움
        print(paymentmeth_art_card)
        print("     system : 카드를 삽입해 주세요.")  # 사용자에게 카드 삽입을 요청
        card = input("     >>> ")
        time.sleep(1)
        if card == "카드" or card == "신용카드":
            clear_console()
            print(pay_complte_art_top)  # 결제 완료 아트 출력
            print(" " * 9, charge_price, "원")  # 결제 금액 출력
            print(pay_complte_art_bottom)  # 결제 완료 아트 하단 출력
            input("     system : 계속하려면 Enter 키를 누르세요.")
            return main()  # 결제 완료, main() 반환
        else :
            print(paymentmeth_card_fail)
            input("     system : 계속하려면 Enter 키를 누르세요.")
            return main()

    # 카카오페이결제
    elif pay_way == "카카오페이":
        clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움
        # 카카오페이 결제 아트 출력
        print(paymentmeth_art_kakao)
        print("     system : 지정된 바코드를 찍어주세요.")  # 사용자에게 바코드를 스캔하도록 요청
        bacord = input("     >>> ")
        time.sleep(1)  # 결제 화면에서 2초 동안 대기 (바코드 스캔을 기다리는 시간)
        if bacord == "바코드":
            clear_console()
            print(pay_complte_art_top)  # 결제 완료 아트 출력
            print(" " * 9, charge_price, "원")  # 결제 금액 출력
            print(pay_complte_art_bottom)  # 결제 완료 아트 하단 출력
            input("     system : 계속하려면 Enter 키를 누르세요.")
            return main()  # 결제 완료, main() 반환
        else :
            print(paymentmeth_kakao_fail)
            input("     system : 계속하려면 Enter 키를 누르세요.")
            return main()

    else:
        # 사용자가 결제 방법을 잘못 입력한 경우
        clear_console()
        print(paymentmeth_fail)  # 결제 실패 아트 출력
        print(f"     system : 결제에 실패했습니다.")  # 결제 실패 메시지 출력
        return False  # 결제 실패, False 반환

#메뉴 db
menu_db = {
    '전체': [
        '콜라', '사이다', '웰치스', '환타', '핫식스', '아메리카노', '녹차', '토레타', '에너지드링크', '커피'
                                                                         '라면', '김밥', '떡볶이', '햄버거', '볶음밥', '샌드위치'
                                                                                                          '라면+콜라',
        '김밥+사이다', '떡볶이+환타', '감자튀김+핫도그+웰치스'
    ],
    '세트': ['라면+콜라', '김밥+사이다', '떡볶이+환타', '감자튀김+핫도그+웰치스'],
    '음료': ['콜라', '사이다', '웰치스', '환타', '핫식스', '아메리카노', '녹차', '토레타', '에너지드링크', '커피'],
    '식사': ['라면', '김밥', '떡볶이', '햄버거', '볶음밥', '샌드위치']
}

price_db = {  # 메뉴별 가격
    '라면+콜라': 5000, '김밥+사이다': 4000, '떡볶이+환타': 3800, '감자튀김+핫도그+웰치스': 6500,
    '콜라': 1800, '사이다': 1800, '웰치스': 1500, '환타': 1500, '핫식스': 1800, '아메리카노': 2000,
    '커피': 2000, '녹차': 1500, '토레타': 1800, '에너지드링크': 2000,
    '라면': 3500, '김밥': 2500, '떡볶이': 3500, '햄버거': 3500, '볶음밥': 4500, '샌드위치': 3000
}

option_db = {  # 옵션 메뉴 (세트, 음료, 식사) 추가
    '세트': ['L', 'M', '감자튀김', '핫도그', '멘보샤', '만두튀김', '순살치킨'],
    '음료': ['L', 'M'],
    '식사': ['감자튀김', '핫도그', '멘보샤', '만두튀김', '순살치킨']
}

option_price_db = {
    '감자튀김': 3000, '핫도그': 2500, '멘보샤': 3500, '만두튀김': 4000, '순살치킨': 5000, 'L': 800, 'M': 0
}


order_counter = 1  # 전역 변수로 시작값 설정
#주문번호 생성 함수
def generate_order_number():
    global order_counter  # 전역 변수 order_counter 사용 선언
    order_number = f"ORD{order_counter:04d}"  # 예: ORD0001, ORD0002 형식의 주문번호 생성
    order_counter += 1  # 주문번호 카운터 증가
    return order_number  # 생성된 주문번호 반환

# 메뉴 카테고리별 목록을 출력하는 함수
def print_menu_art(category):
    # 선택한 카테고리에 맞는 메뉴를 출력
    if category == "전체":
        print(menu_list_all)  # 모든 메뉴 리스트
    elif category == "세트":
        print(menu_list_set)  # 세트 메뉴 리스트
    elif category == "음료":
        print(menu_list_drink)  # 음료 메뉴 리스트
    elif category == "식사":
        print(menu_list_food)  # 식사 메뉴 리스트
    elif category == "사이드":
        print(menu_list_food_side)  # 사이드 메뉴 리스트
    else:
        print("     system : 해당 카테고리의 메뉴가 없습니다.")  # 잘못된 카테고리 입력 시

cart = []  # 장바구니를 담을 리스트
# 메뉴 리스트를 보여주는 함수
def menu_list():
    clear_console() # 콘솔 화면을 깨끗하게 지웁니다.
    # 카테고리 선택
    while True:
        clear_console()
        print("     카테고리를 선택하세요")
        print(menu_list_art)  # 메뉴 카테고리 목록 출력
        print("     system : 번호 입력 또는 카테고리명 입력")
        cat_choice = input("     >>> ").strip()  # 카테고리 선택 (번호 또는 이름)

        categories = list(menu_db.keys())  # 카테고리 목록을 가져옴
        if cat_choice.isdigit():  # 사용자가 번호를 입력했다면
            cat_idx = int(cat_choice) - 1
            if 0 <= cat_idx < len(categories):  # 입력한 번호가 유효한 범위인지 확인
                category = categories[cat_idx]  # 해당 카테고리 선택
            else:
                print("     system : 올바른 번호를 입력하세요.")  # 범위 밖 번호 입력 시
                continue
        else:  # 사용자가 카테고리명을 입력했다면
            if cat_choice in menu_db:
                category = cat_choice  # 해당 카테고리 선택
            else:
                print("     system : 올바른 카테고리를 입력하세요.")  # 잘못된 카테고리명 입력 시
                continue

        clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
        print_menu_art(category)  # 선택된 카테고리에 맞는 메뉴 출력
        break  # 카테고리 선택 후 종료

    # 메뉴 입력 (선택한 카테고리 내에서)
    while True:
        print("     system :메뉴를 입력하세요 (여러 개: 콤마로 구분)")
        user_input = input("     >>> ")  # 여러 메뉴를 입력받음
        user_choices = [item.strip() for item in user_input.split(',')]  # 콤마로 구분된 메뉴를 리스트로 저장
        selected_menus = []

        for choice in user_choices:
            if choice in menu_db[category] or (
                    category == '전체' and any(choice in menu_db[c] for c in ['세트', '음료', '식사'])):
                selected_menus.append(choice)  # 유효한 메뉴만 선택
            else:
                print(f"     system : ❌ 해당 메뉴가 없습니다: {choice}")  # 잘못된 메뉴 선택 시
        if not selected_menus:
            print("     system : 선택한 유효한 메뉴가 없습니다.")
            continue  # 유효한 메뉴가 없으면 다시 선택

        print("     system : ✅ 선택한 메뉴 >>>", selected_menus)  # 유효한 메뉴 출력
        break  # 메뉴 선택 완료 후 종료

    # 옵션 선택 및 장바구니 담기
    for menu in selected_menus:
        menu_category = None
        for cat in ['세트', '음료', '식사']:
            if menu in menu_db[cat]:
                menu_category = cat  # 해당 메뉴가 어떤 카테고리에 속하는지 찾음
                break

        if menu_category and menu_category in option_db:
            print(
                f"\n     [옵션 선택] {menu} ({menu_category})\n     사용 가능한 옵션\n     {'\n     '.join(option_db[menu_category])}")
            print("     system : 콤마로 구분, 입력할 옵션이 없다면 Enter을 눌러주세요")
            option_input = input("     >>> ")  # 옵션 입력 받기
            option_input = [opt.strip() for opt in option_input.split(',') if opt.strip()]  # 콤마로 구분된 옵션
            selected_options = [opt for opt in option_input if opt in option_db[menu_category]]  # 유효한 옵션만 선택
        else:
            selected_options = []  # 옵션이 없다면 빈 리스트

        quantity = input(f"     system : {menu} 수량을 입력해주세요: ").strip()  # 수량 입력 받기
        quantity = int(quantity) if quantity.isdigit() and int(quantity) > 0 else 1  # 수량이 유효하지 않으면 기본값 1

        cart.append({
            '메뉴': menu,
            '옵션': selected_options,
            '수량': quantity  # 선택한 수량을 장바구니에 추가
        })

    # 장바구니 출력 및 총 결제 금액 계산
    total_price = 0  # 총 결제 금액 넣을 변수 초기화
    clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
    print(cart_art_top)
    total_price = 0
    for item in cart:
        menu_name = item['메뉴']
        base_price = price_db.get(menu_name, 0)  # 메뉴 기본 가격
        option_list = item['옵션']  # 선택된 옵션
        quantity = item['수량']  # 수량

        option_price = sum(option_price_db.get(opt, 0) for opt in option_list)  # 옵션 가격 합산
        item_total = (base_price + option_price) * quantity  # 메뉴의 총 금액 (기본 가격 + 옵션 가격) * 수량
        total_price += item_total  # 총 금액에 합산

        option_str = ', '.join(option_list) if option_list else '없음'  # 옵션이 있을 경우 옵션 문자열 생성
        print(" " * 8, f"메뉴 : {menu_name}x{quantity}({base_price}원)", "\n", " " * 7,
              f"옵션 : {option_str}({option_price}원)")
        print()
    print(" " * 4, f"💰 총 결제 금액: {total_price}원")  # 총 결제 금액 출력

    # 장바구니에 음식을 더 담을지 여부 묻기
    while True:
        print(" " * 4, "system : 장바구니에 음식을 더담으시겠습니까?(Y/N)")
        yes_no = input("     >>> ").strip().lower()  # 사용자 입력 받기 (대소문자 구분 없이 처리)

        if yes_no == 'y':  # 'y' 입력 시, 메뉴 리스트를 다시 호출
            return menu_list()
        elif yes_no == 'n':  # 'n' 입력 시, 장바구니 수정/결제 과정으로 진행
            break
        else:  # 잘못된 입력을 받은 경우
            print("     system : 입력을 다시 해주세요.")
            continue

    # (이후 결제 및 장바구니 수정 코드)
    while True:
        print("     system : 장바구니에서 삭제할 메뉴가 있습니까? (Y/N)")  # 장바구니에서 삭제할 메뉴가 있는지 묻기
        yes_no = input("     >>> ").strip().lower()  # 사용자 입력 받기

        if yes_no == 'y':  # 'y' 입력 시, 삭제할 메뉴 리스트를 표시
            for idx, item in enumerate(cart, 1):  # 장바구니에 담긴 메뉴 항목 출력
                print(f"{idx}. {item['메뉴']} x{item['수량']} / 옵션: {', '.join(item['옵션'])}")

            # 사용자에게 삭제할 항목 번호 입력 받기
            del_idx = int(input("     system : 삭제할 항목 번호 입력: ")) - 1

            # 유효한 번호가 입력되었는지 확인
            if 0 <= del_idx < len(cart):
                del cart[del_idx]  # 유효한 번호라면 해당 항목 삭제
            else:
                print("     system : 다시 입력해주세요.")  # 유효하지 않은 번호 입력 시 다시 입력 받기
                del_idx = int(input("     system : 삭제할 항목 번호 입력: ")) - 1
                del cart[del_idx]

            # 장바구니가 비었을 때 처리
            if not cart:
                print("\n     system : 장바구니가 비었습니다 다시 메뉴를 선택해주세요.")
                return menu_list()  # 장바구니가 비었을 때 메뉴 선택창으로 돌아가기

        elif yes_no == 'n':  # 'n' 입력 시, 더 이상 삭제하지 않음
            break
        else:  # 잘못된 입력을 받은 경우
            print("     system : 입력을 다시 해주세요.")
            continue

        # 삭제 후 장바구니 금액 재계산
        total_price = 0  # 총 금액을 초기화
        clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
        print("\n🛒 [수정된 장바구니]")  # 수정된 장바구니 제목 출력

        # 장바구니에 있는 각 항목에 대해 반복
        for item in cart:
            menu_name = item['메뉴']  # 항목의 메뉴 이름
            base_price = price_db.get(menu_name, 0)  # 메뉴의 기본 가격을 price_db에서 가져옴. 없으면 기본값 0
            option_list = item['옵션']  # 해당 메뉴의 옵션 목록
            quantity = item.get('수량', 1)  # 메뉴의 수량을 가져옴. 없으면 기본값 1

            # 옵션이 있을 경우, 옵션에 대한 추가 가격을 합산
            option_price = sum(option_price_db.get(opt, 0) for opt in option_list)
            # 해당 메뉴의 총 금액 (기본 가격 + 옵션 가격) * 수량
            item_total = (base_price + option_price) * quantity
            total_price += item_total  # 장바구니의 총 금액에 항목의 금액을 더함

            # 옵션이 있을 경우 그 옵션들을 나열. 옵션이 없으면 '없음' 출력
            option_str = ', '.join(option_list) if option_list else '없음'

            # 각 메뉴 항목과 해당 항목의 총합을 출력
            print(
                f"- {menu_name}x{quantity} ({base_price}원) + 옵션({option_price}원) → 합계: {item_total}원 / 옵션: {option_str}")
        # 장바구니의 모든 항목을 계산한 후, 최종 총 결제 금액 출력
        print(f"\n     system : 💰 [수정된 총 결제 금액]: {total_price}원")

    clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.

    # 결제 진행 (menu_pay 함수에서 결제 로직 수행, 성공하면 True 반환)
    if menu_pay(str(total_price)):
        order_number = generate_order_number()  # 주문 번호 생성
        print(f"\n     ✅ 주문이 완료되었습니다.")  # 성공 메시지 출력
        print(f"     📦 주문번호: {order_number}")  # 주문번호 출력
        cart.clear()  # 장바구니 초기화
    else:
        print("\n     ❌ 주문이 취소되었습니다.")  # 결제 실패 시 메시지 출력

    # 성공/실패와 상관없이 메인 화면으로 돌아가기 전에 사용자 입력 대기
    input("     system : 계속하려면 Enter 키를 누르세요.")
    clear_console()  # 콘솔 화면 정리
    main()  # 메인 화면으로 이동


# 메뉴결제관리함수
def menu_pay(total_price):
    while True:
        clear_console()
        print(paymentmeth_art)
        print("     지불할 금액은", total_price, "원 입니다. ")  # 결제 금액 출력
        print("     system : 결제방식 입력")
        menu_pay_way = int(input("     >>> "))  # 결제 방식 선택

        lst = ["취소하기", "현금", "신용카드", "카카오페이"]

        if menu_pay_way == 0:  # 취소하기
            # print("     system : 취소하겠습니다.")
            cart.clear()
            return 0  # 결제 진행하지 않음

        if 1 <= menu_pay_way <= 3:
            menu_pay_way = lst[menu_pay_way]  # 결제 방법 리스트에서 선택된 결제 방식

        # 현금결제
        if menu_pay_way == "현금":
            while True:
                clear_console()
                print(paymentmeth_art_cash)
                print("     지불할 금액은", total_price, "원 입니다. ")
                print("     system : 현금을 넣어 주세요")
                money = int(input("     >>> "))  # 현금 입력 받기
                if money == 0:
                    clear_console()
                    print(paymentmeth_cash_fail)
                    print("     system : ❌ 현금이 부족하여 결제가 취소되었습니다.")
                    return False  # 결제 취소
                elif int(total_price) <= money:
                    clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움
                    change_money = money - int(total_price)
                    print(pay_complte_art_top)
                    print(" " * 9, total_price, "원")  # 결제 아트 편집
                    print(pay_complte_art_bottom)
                    print("     거스름돈 >>> ", change_money)  # 거스름돈 계산
                    cart.clear()
                    time.sleep(2)
                    return True  # 결제 완료
                else:
                    clear_console()
                    print(paymentmeth_cash_fail)
                    print("     system : ❌ 금액이 부족합니다. 다시 시도해 주세요.")
                    continue  # 다시 현금 입력 받기
        # 신용카드결제
        elif menu_pay_way == "신용카드":
            while True:
                clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움
                print(paymentmeth_art_card)
                print("     system : 카드를 삽입해 주세요.")
                print("     지불할 금액은", total_price, "원 입니다. ")
                card = input("     >> ")
                time.sleep(1)  # 결제 화면에서 2초 동안 대기 (바코드 스캔을 기다리는 시간)
                if card == "카드" or card == "신용카드":
                    clear_console()
                    print(pay_complte_art_top)
                    print(" " * 9, total_price, "원")
                    print(pay_complte_art_bottom)
                    # clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
                    cart.clear()
                    time.sleep(2)
                    return True  # 결제 완료 후 메인 화면으로 돌아가기
                else:
                    clear_console()
                    print(paymentmeth_card_fail)
                    input("     계속하려면 Enter 키를 누르세요.")
                    cart.clear()
                    continue
        # 카카오페이결제
        elif menu_pay_way == "카카오페이":
            while True:
                clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움
                print(paymentmeth_art_kakao)
                print("     지정된 바코드를 찍어주세요.")
                print("     지불할 금액은", total_price, "원 입니다. ")
                bacord = input("    >>> ")
                time.sleep(1)  # 결제 화면에서 2초 동안 대기 (바코드 스캔을 기다리는 시간)
                if bacord == "바코드":
                    clear_console()
                    print(pay_complte_art_top)
                    print(" " * 9, total_price, "원")
                    print(pay_complte_art_bottom)
                    # clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
                    cart.clear()
                    time.sleep(2)
                    return True  # 결제 완료 후 메인 화면으로 돌아가기
                else:
                    clear_console()
                    print(paymentmeth_kakao_fail)
                    input("     system : 계속하려면 Enter 키를 누르세요.")
                    cart.clear()
                    continue
        # 결제실패
        else:
            clear_console()
            print(paymentmeth_fail)
            print(f"     System : 결제에 실패했습니다. 다시 결제 수단을 선택합니다.")
            time.sleep(2)
            continue


# 메인선택화면함수
def main_screen():
    while True:
        print(main_art)  # 메인 화면에 출력되는 아트 출력
        print("     system : 메뉴를 입력하세요.")
        menu_choice = input("     >>> ")  # 사용자로부터 메뉴 선택 받기

        # 선택된 메뉴에 따라 분기
        if menu_choice == "1":
            result = rate_plan()  # '1'번 메뉴를 선택한 경우 rate_plan() 함수 호출
            if result == "to_main":
                return  # 'to_main'이 반환되면 로그인 화면으로 돌아가도록 함
        elif menu_choice == "2":
            menu_list()  # '2'번 메뉴를 선택한 경우 메뉴 목록 화면으로 이동
        elif menu_choice == "3":
            clear_console()
            print("     system : 종료합니다.")  # '3'번 메뉴를 선택한 경우 종료 메시지 출력
            exit()
        else:
            # 잘못된 메뉴 입력 시 오류 메시지 출력
            print("     system : 올바른 메뉴를 입력하세요.")
            input("     system : 계속하려면 Enter 키를 누르세요.")  # 다시 선택하도록 대기
        clear_console()  # 메뉴 선택 후 콘솔 화면을 깨끗이 지움


# 메인로그인함수
def main():
    while True:
        clear_console()  # 콘솔 화면을 깨끗하게 지웁니다.
        print(main_login_art)  # 로그인 화면에 출력되는 아트 출력
        print("      system : 메뉴를 선택하세요.")
        choice = input("      >>> ")  # 사용자로부터 메뉴 선택 받기

        # 사용자 입력에 따라 분기
        if choice == '1':
            # '1'번을 선택한 경우 로그인 함수를 호출하고 성공하면 메인 화면으로
            if login():
                main_screen()  # 로그인 성공 후 메인 화면으로 이동
        elif choice == '2':
            # '2'번을 선택한 경우 비회원 로그인 함수를 호출하고 성공하면 메인 화면으로
            if guest_login():
                main_screen()  # 비회원 로그인 성공 후 메인 화면으로 이동
        elif choice == '3':
            clear_console()
            print("     system : 종료합니다.")
            exit()
        else:
            # 잘못된 메뉴 선택 시 오류 메시지 출력
            print("     system : 올바른 메뉴를 선택해주세요.")
            input("     system : 계속하려면 Enter 키를 누르세요.")  # 다시 선택하도록 대기

#실행
main()