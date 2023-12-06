from dataset import cut_video, check_metadata
from yolo import yolo_train, yolo_test_by_image, yolo_test_by_live, yolo_val

if __name__ == "__main__":
    # cut_video('E:\\오픈소스SW기초 보행등 데이터 셋\\OTL Night Dataset.mp4', 'tld_night_', 5)
    # check_metadata('./target/red')
    yolo_train()
    # yolo_test_by_image('PATH')
    # yolo_test_by_live()
    # yolo_val()
    pass
