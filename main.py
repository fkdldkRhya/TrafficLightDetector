from dataset import cut_video, check_metadata
from yolo import yolo_train

if __name__ == "__main__":
    # cut_video('C:/Users/ji055/Desktop/tl_videos/red/RED.mp4', 'tld_red_', 5)
    # check_metadata('./target/red')
    yolo_train()
