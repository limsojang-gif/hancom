import streamlit as st
from ultralytics import YOLO
import cv2
import pandas as pd
import plotly.express as px
import time

# 1. 화면 구성 - 화면을 좌우 2칸으로 나눔 
col1, col2 = st.columns(2)        #같은 너비 두 칸 만들기
with col1 : 
    frame_placeholder = st.empty()  #프레임 화면 

with col2 :
    chart_placeholder = st.empty()  #그레프 화면

# 2. 비디오 경로 설정 - cctv  주소 연결 

stream_url = "http://210.99.70.120:1935/live/cctv013.stream/playlist.m3u8"

cap = cv2.VideoCapture(stream_url)

# 3. 모델 로드
@st.cache_resource  # 모델이나 DB 같은 무거운 자원 캐싱 
def load_model():
    return YOLO("yolo11n.pt")

model = load_model()

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("FRAME FAIL")
        break

    # 4-1 모델 객체 탐지 수행
    results = model(frame)

    # 4-2 탐지 결과
    annotated_frame = results[0].plot()

    # 4-3 탐지된 객체의 클레스 이름 추출 -"사람", "차"
    labels =[model.names[int(c)] for c in results[0].boxes.cls]
            # 컴프리헨션으로 클레스 이름 가져오기

    # 4-4 탐지 객체 시각화 - 종류별 개수 세서 막대그래프 만듬
    if labels: #객체 탐지 된다면
        #labels 리스트를 dataframe 으로 변환 후 개수 집개
        df_count = pd.DataFrame({"Object" : labels})

        #종류별 개수 세기
        df_count = df_count.value_counts().reset_index(name="count")

        #plotly 이용해 막대 그래프 생성
        fig = px.bar(
            df_count,
            x="Object",
            y="count",
            title="탐지 객체 수",
            color="Object",
            text="count"
        )
    else: 
        df_count =pd.DataFrame({"Object": [], "Count":[]})
        #빈 표만 표시
        fig = px.bar(
            df_count,
            x="Object",
            y="count",
            title="탐지 객체 수"
        )

    # 4-5  결과 표시 - 왼쪽 영상 오른쪽 그레프
    frame_placeholder.image(annotated_frame, channels="BGR")
    chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"chart_{time.time()}")
    #매번 다른 키 값 설정 위잿 충돌 막기 

# 5 자원 해제
cap.release()
cv2.destroyAllWindows()


