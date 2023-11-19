from ultralytics import YOLO


def yolo_val():
    model = YOLO("./runs/detect/yolov8n_SVTLv6/weights/best.pt")
    model.val()
