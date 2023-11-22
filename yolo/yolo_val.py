from ultralytics import YOLO


def yolo_val():
    model = YOLO("./runs/detect/yolov8n_SVTLv6_da_scale/weights/best.pt")
    model.info()
    model.val()
