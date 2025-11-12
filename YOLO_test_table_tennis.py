from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

model.predict(source="data/validation/images", save=True, device="mps")