from ultralytics import YOLO


def yolo_train():
    # Load the model.
    model = YOLO('yolov8n.pt')

    # Training.
    results = model.train(
        data='./yolo_config.yaml',
        imgsz=640,
        epochs=8,
        batch=8,
        name='yolov8n_SVTLv6',
        workers=4,
    )

    print(results)
