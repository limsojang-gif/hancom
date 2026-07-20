from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

model(
    "input_seg.jpg",
    classes=[60, 75],
    conf=0.5,
    save=True,
    project="runs/detect",
    name="predict"
)