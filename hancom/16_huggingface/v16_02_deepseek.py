import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# .env 파일의 HF_TOKEN 읽기
load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    print("HF_TOKEN을 찾을 수 없습니다.")
    print(".env 파일을 확인하세요.")
    raise SystemExit

client = InferenceClient(
    provider="novita",
    api_key=token,
    timeout=60
)

answer = input("질문을 입력해 주세요: ")

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2",
    messages=[
        {
            "role": "user",
            "content": answer
        }
    ],
    max_tokens=512
)

print(completion.choices[0].message.content)