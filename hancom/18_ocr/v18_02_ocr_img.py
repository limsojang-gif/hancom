import pytesseract
from PIL import Image

# Tesseract 실행 파일 경로
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# 이미지 불러오기
image = Image.open("image.png")

# OCR 수행: 한국어 언어 코드 = kor
results = pytesseract.image_to_string(
    image,
    lang="kor"
)

print("=======================================")
print(results)
print("=======================================")