# ======================================
# 1. 클래스 : 제품의 설계도 
# 2. 생성자 : 객체를 만들 떄 실행되는 함수 
# 3. 속성 : 클래스 안에 변수 
# 4. 메서드 : 클레스 안의 함수 
# 5. 객체 : 설계도로 만든 제품
#=======================================

# 클레스 정의 
class World:
    # 생성자 
    def __init__(self, name,):
        # 속성 
        self.name = name

    def hello(self):
        print(f"Hello! {self.name}!Welcom!")

# 객체 생성
asia = World("Korea")
asia.hello()
