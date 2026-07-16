name = ["뽀삐", "초코", "쿠키"]
scores = [95, 88, 72]

# for name, score in zip(name, scores): 
#     print(f"{name} : {score}")
# 결과
# 뽀삐 : 95
# 초코 : 88
# 쿠키 : 72
    # zip 이름과 점수가 따로 떨어진 두 리스트를, 
    # 지퍼처럼 한 칸씩 같은 자리끼리 맞물려 한 쌍으로 묶어주는 함수

# pairs = list(zip(name, scores))
# print(pairs)
# # 결과
# #[('뽀삐', 95), ('초코', 88), ('쿠키', 72)]

# keys = ["이름", "나이", "직업"]  #dict 는 keys 값으로 묶임
# vlaues = ["홍", 30, "개발자"]

# person = dict(zip(keys, vlaues))
# print(person)
# # 결과 
# # {'이름': '홍', '나이': 30, '직업': '개발자'}