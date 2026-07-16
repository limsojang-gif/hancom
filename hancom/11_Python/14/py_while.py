def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

while True:
    # 사용자 입력 부분
    user_input = input("미터 값을 입력하세요 : ")

    # 예외 처리 
    try: 
        meters = float(user_input)
        feet = meters_to_feet(meters)
        print(f"{meters}m는 {feet}ft 입니다")
        break  #  - 숫자를 제대로 입력하면 키터 값을 입력하시오 나오지 않게함
                # break는 멈춤 버튼 — while 안에서 만나면 반복을 즉시 멈추고 빠져나옴

    except ValueError:
        print("숫자를 입력해 주세요.")

        # 미터 값을 입력하세요 : ㅇㅀㅀ
        # 숫자를 입력해 주세요.
        # 미터 값을 입력하세요 : 