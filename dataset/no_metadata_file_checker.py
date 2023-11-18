import os


def check_metadata(path):
    files = os.listdir(path)

    count = 0

    for file in files:
        if file.endswith('.jpg'):
            if not os.path.exists(path + '/' + file[:-4] + '.txt'):
                print('No metadata file:', file)

                os.remove(path + '/' + file)
                print('[-] Removed:', file)

                count += 1

    print('Total:', count)