from transformers import pipeline

# 1. 요약 파이프라인 생성 

summarizer = pipeline(
    "summarization",
    model="t5-small"
)
# 2. 요약할 원문

text = """
From the author of The Martian, a lone astronaut must save the earth from disaster in this “propulsive” (Entertainment Weekly), cinematic thriller full of suspense, humor, and fascinating science.

"""
# 3. 요약 실행
summary = summarizer(
    text,
    min_length=20,
    max_length=60,
    do_sample=False
)
# 4. 결과 확인
sum_text = summary[0]['summary_text']
print(f"요약된 문장 {sum_text}")

""""
요약된 문장 a lone astronaut must save the earth from disaster in this "propulsive" thriller . the thriller is full of suspense, humor, and science fiction 
"""
