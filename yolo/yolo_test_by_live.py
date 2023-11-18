import datetime

import cv2
from ultralytics import YOLO


def yolo_test_by_live():
    model = YOLO("./runs/detect/yolov8n_STLv6/weights/best.pt")
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 940)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 780)

    CONFIDENCE_THRESHOLD = 0.6
    class_list = ["tld_green", "tld_red"]
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)

    while True:
        start = datetime.datetime.now()

        ret, frame = cap.read()
        if not ret:
            print('Cam Error')
            break

        detection = model(frame)[0]

        for data in detection.boxes.data.tolist():
            confidence = float(data[4])
            if confidence < CONFIDENCE_THRESHOLD:
                continue

            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            label = int(data[5])
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
            cv2.putText(frame, class_list[label] + ' ' + str(round(confidence, 2)) + '%', (xmin, ymin), cv2.FONT_ITALIC,
                        1, WHITE, 2)

        end = datetime.datetime.now()

        total = (end - start).total_seconds()
        print(f'Time to process 1 frame: {total * 1000:.0f} milliseconds')

        fps = f'FPS: {1 / total:.2f}'
        cv2.putText(frame, fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow('yolo_test_by_live', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
