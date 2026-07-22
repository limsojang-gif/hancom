from transformers import pipeline
from deep_translator import GoogleTranslator


# 영어 문장을 한국어로 번역하는 함수
def trans_en_to_ko(sentence):
    return GoogleTranslator(source="en", target="ko").translate(sentence)


# 1. 요약 파이프라인 생성
summarizer = pipeline(
    "summarization",
    model="t5-small"
)

# 2. 요약할 원문
text = """
His crewmates dead, his memories fuzzily returning, Ryland realizes that an impossible task now confronts him. Hurtling through space on this tiny ship, it’s up to him to puzzle out an impossible scientific mystery—and conquer an extinction-level threat to our species.
And with the clock ticking down and the nearest human being light-years away, he’s got to do it all alone.
Or does he?
"""

# 3. 영어 문장 요약
summary = summarizer(
    "summarize: " + text,
    min_length=20,
    max_length=60,
    do_sample=False
)

# 4. 요약 결과 추출
sum_text = summary[0]["summary_text"]
print(f"영어 요약: {sum_text}")

# 5. 요약문을 한국어로 번역
kr_sum_text = trans_en_to_ko(sum_text)

# 6. 한국어 번역문 출력
print(f"한국어 요약: {kr_sum_text}")

# """
# 영어 요약: the author of The Martian must save the earth from disaster in this cinematic thriller full of suspense, humor, and science .

# 한국어 요약: The Martian의 작가는 서스펜스, 유머, 과학이 가득한 이 영화 같은 스릴러에서 재난으로부터 지구를 구해야 합니다 .
# """

# python -m pip install deep-translator  설치 필요