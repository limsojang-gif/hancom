from transformers import pipeline  
#pipline  : 텍스트 이미지 등 다양한  ai  테스크를 쉽게 실행할 수 있ㄴ느 도구

# 1. 감정 분석 파이프라인 생성 
classifier = pipeline("sentiment-analysis")

# 2. 감정 분석할 문장 입력
text = " she go to school "
results = classifier(text)


# 3. 결과 확인
print(f"감정 분석 결과 : {results[0]['label']}")
print(f"감정 분석 점수 : {results[0]['score']:.4f}")

# 감정 분석 결과 : POSITIVE
# 감정 분석 점수 : 0.9808
# 감정 분석 결과 : NEGATIVE
# 감정 분석 점수 : 0.9988