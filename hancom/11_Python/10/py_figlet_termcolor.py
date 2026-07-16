# 1. pyfiglet, termcolor 불러오기 
# 2. pyfiglet 적용
# 3. termcolor 적용
# 4. pyfiglet + termcolor 적용

# import pyfiglet
# from termcolor import colored

# sentence = "HI ! HI"
# py_sentence = pyfiglet.figlet_format(sentence) 
# print(py_sentence)


# color_ho = colored("I'm SJ", "green",)
# print(color_ho)
import pyfiglet
from termcolor import colored

py_text = pyfiglet.figlet_format("SO JANG")
color_text = colored(py_text, "blue", "on_yellow")
print(color_text)