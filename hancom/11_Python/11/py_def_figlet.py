import pyfiglet
from termcolor import colored

def good_sentence(sentence: str) -> None:
    """
    입력된 문자를 pyfiglet  형식으로 출력 
    파라미터 : sentence(str)
    반환 : None-출력만 수향
    """

    py_sentence = pyfiglet.figlet_format(sentence)
    print(py_sentence)

good_sentence("ONLY EG")


