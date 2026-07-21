from ultralytics import FastSAM
from pathlib import Path
import cv2

# 현재 Python 파일이 있는 폴더
base_dir = Path(__file__).resolve().parent

# 이미지와 모델 경로
source = base_dir / "image.png"
model_path = base_dir / "FastSAM-s.pt"

print("이미지 경로:", source)
print("이미지 존재:", source.exists())

if not source.exists():
    print("image.png 파일을 찾을 수 없습니다.")
    raise SystemExit

if not model_path.exists():
    print("FastSAM-s.pt 파일을 찾을 수 없습니다.")
    raise SystemExit

# 모델 로드
model = FastSAM(str(model_path))

# 모든 객체 분할 -찾고 싶은것 
results =  model(
    str(source),
    points=[[180, 255]],
    labels=[1]
)

# 결과 저장
output_path = base_dir / "output_result.jpg"
output_image = results[0].plot()

save_success = cv2.imwrite(str(output_path), output_image)

if save_success:
    print(f"이미지가 저장됨: {output_path}")
else:
    print("결과 이미지 저장 실패")