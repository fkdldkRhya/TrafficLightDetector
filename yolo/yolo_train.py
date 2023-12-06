from ultralytics import YOLO


def yolo_train():
    # Load the model.
    model = YOLO('../runs/detect/yolov8n_SVTLv7_da_fusion/weights/best.pt')

    # Training.
    results = model.train(
        data='./yolo_config.yaml',
        imgsz=640,
        epochs=8,
        batch=8,
        name='yolov8n_SVTLv7_da_fusion4',
        workers=5,
    )

    print(results)
