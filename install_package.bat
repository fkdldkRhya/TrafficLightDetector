@echo off_

pip install opencv-python

pip install ultralytics

pip install matplotlib

pip uninstall torch
pip uninstall torchvision

pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html