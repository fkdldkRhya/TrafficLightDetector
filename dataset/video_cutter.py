import cv2
import os


def cut_video(filepath, fi_name, input_fps):
    print('OpenCV-Version:', cv2.__version__)

    video = cv2.VideoCapture(filepath)

    if not video.isOpened():
        print("Could not Open :", filepath)
        exit(0)

    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print("length :", length)
    print("width :", width)
    print("height :", height)
    print("fps :", fps)

    try:
        if not os.path.exists(filepath[:-4]):
            os.makedirs(filepath[:-4])
    except OSError:
        print('Error: Creating directory. ' + filepath[:-4])

    count = 0

    if input_fps == 0:
        input_fps = fps

    while video.isOpened():
        if count > length:
            break

        ret, image = video.read()
        if int(video.get(1)) % input_fps == 0:
            cv2.imwrite(filepath[:-4] + "/%sframe%d.jpg" % (fi_name, count), image)
            print('Saved frame number :', str(int(video.get(1))), ' / ', str(length))
            count += 1

    print("Completed!")
    print("Saved total frame :", count)

    video.release()
    exit(0)
