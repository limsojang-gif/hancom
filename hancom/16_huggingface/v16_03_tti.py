import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="auto",
    api_key="허그페이스에서 받은 키 넣기",
)

# 사용자 입력 받기 
answer = input("생성이미지를 성멸해 주세요 : ")

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="black-forest-labs/FLUX.1-dev",
)

#생성 이미지 저장
image.save("tti_result.jpg")


print("전체 코드가 잘 실행됐습니다.")