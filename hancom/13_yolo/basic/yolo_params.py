from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model(
    "input_params.jpg",
    classes=[60, 75],
    conf=0.5,        # 여기에 쉼표 추가
    save=True
)