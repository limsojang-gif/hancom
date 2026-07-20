import cv2  #카메라 다루는 도구
import os    # 폴더 만드는 도구 
from datetime import datetime # 지금 시간 알려주는 도구

# 1. 사진 저장 폴더 준비
save_dir = "./captured_images"
os.makedirs(save_dir, exist_ok=True) #폴더가 없으면 자동으로 생성

# 2. 카메라를 킨다. 
cap = cv2.VideoCapture(0)

# 3. 사진을 한 장 찍기
success, frame = cap.read()
if success:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 예 2026720_
    file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")

    #파일로 저장 
    cv2.imwrite(file_path, frame)
    print(f"사진이 저장!{ file_path}")
else:
    print("카메라를 못 읽었습니다")

# 4. 카메라 끄기
cap.release()