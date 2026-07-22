from transformers import pipeline

# 1. 텍스트 생성 파이프라인 생성
generator = pipeline("text-generation", model="gpt2")  # 기본 영어 모델

# 2. 시드 문장 입력
answer = input("생성 문장을 입력해주세요 : ")

# 3. 텍스트 생성 실행
results = generator(
    answer,
    max_length=100,           # 최대 토큰 길이
    num_return_sequences=1,
    do_sample=True            # 다양한 생성을 위해 샘플링 사용
)
# 4. 결과 확인

print(results[0]['generated_text'])