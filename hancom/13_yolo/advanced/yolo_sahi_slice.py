from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel
import os

# 1. 모델 및 이미지 경로
model_path = "yolo11n.pt"
image_path = "demo_data/image_1.png"

if not os.path.exists(image_path):
    print(f"이미지 파일이 없습니다: {os.path.abspath(image_path)}")
    raise SystemExit

# 2. 모델 로드
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path,
    confidence_threshold=0.4
)

# 3. SAHI 적용
results = get_sliced_prediction(
    image_path,
    detection_model,
    slice_width=200,
    slice_height=200,
    overlap_width_ratio=0.1,
    overlap_height_ratio=0.1
)

# 4. 결과 이미지 저장
results.export_visuals(export_dir="sahi/")

# 5. 탐지 개수 출력
detected_count = len(results.object_prediction_list)

print(f"탐지 수: {detected_count}")
print("모든 코드가 성공적으로 수행됐습니다.")