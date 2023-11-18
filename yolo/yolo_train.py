from ultralytics import YOLO


def yolo_train():
    # Load the model.
    model = YOLO('yolov8n.pt')

    # Training.
    results = model.train(
        data='./yolo_config.yaml',
        imgsz=640,
        epochs=10,
        batch=8,
        name='yolov8n_custom',
        workers=0,
    )

    print(results)