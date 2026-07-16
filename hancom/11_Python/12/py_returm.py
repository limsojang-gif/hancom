from termcolor import colored

def highlight(text:str, color:str) -> str:
    """
    text, color 를 입력받아 text  색상을 변경하는 함수 

    text :str
    color :str
    """

    color_text =colored(text, color)
    return color_text

#보이는법 2가지 
# 1
# results =highlight("GO GO !! Home", "green")
# print(results)

# 2
print(highlight("GO GO !! Home", "green"))



# 계산기에 숫자를 누르면 답이 화면에 나타나듯, return은 함수가 만든 결과를 바깥으로 건네주는 명령어.
# print처럼 그냥 보여주는 것이 아니라, 결과를 변수에 담아 다른 곳에서도 쓸 수 있게 해줌
