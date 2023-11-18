import cv2
from ultralytics import YOLO


def yolo_test_by_image(path):
    model = YOLO("./runs/detect/yolov8n_custom/weights/best.pt")

    results = model.predict(path, line_thickness=2)
    res_plot = results[0].plot()
    cv2.imshow('yolo_test_by_image', res_plot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
