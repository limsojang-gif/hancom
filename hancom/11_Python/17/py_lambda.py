# 람다 공식 
# 함수명 = lambda  매개변수(파라미터) : 반환값

# def add(a,b):
#     return a + b
# print(add(7, 3))
# #10

#위에것을 람다함수로 만들어보기 

# add = lambda a,b : a + b
# print(add(7,3))
# #10

# 글자를 넣으면  큰 그림 글씨로 출력 (pyfiglet)해주는 lambda 함수 

# from pyfiglet import figlet_format
# from termcolor import colored

# big_text = lambda text, font="standard", color="blue": colored(
#     figlet_format(text, font=font),
#     color
# )
# print(big_text("HAPPY", "big","magenta"))

#  _    _          _____  _______     __
# | |  | |   /\   |  __ \|  __ \ \   / /
# | |__| |  /  \  | |__) | |__) \ \_/ / 
# |  __  | / /\ \ |  ___/|  ___/ \   /  
# | |  | |/ ____ \| |    | |      | |   
# |_|  |_/_/    \_\_|    |_|      |_|   
                                      

import pyfiglet

def decorate_text(text):
    return pyfiglet.figlet_format(text)

decorate_text = lambda text : pyfiglet.figlet_format(text)
print(decorate_text("LAMBDA"))

#  _        _    __  __ ____  ____    _    
# | |      / \  |  \/  | __ )|  _ \  / \   
# | |     / _ \ | |\/| |  _ \| | | |/ _ \  
# | |___ / ___ \| |  | | |_) | |_| / ___ \ 
# |_____/_/   \_\_|  |_|____/|____/_/   \_\
#                                         #  

