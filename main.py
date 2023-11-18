import os

from dataset import cut_video, check_metadata
from yolo import yolo_train, yolo_test_by_image, yolo_test_by_live

if __name__ == "__main__":
    # cut_video('./RED.mp4', 'tld_red_', 5)
    # check_metadata('./target/red')
    # yolo_train()
    # 파일 읽기
    path = 'C:/Users/ji055/Desktop/A'
    for a in os.listdir(path):
        if a.endswith('.jpeg') or a.endswith('.jpg') or a.endswith('.png'):
            yolo_test_by_image('%s/%s' % (path, a))
    # yolo_test_by_live()
    pass
