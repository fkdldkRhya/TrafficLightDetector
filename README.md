# TrafficLightDetector
한양대학교 ERICA 스마트융합공학부 - 보행등 분류 프로젝트

## 프로젝트 개요
- 시각 장애인을 위한 간이 보행등 만들기 프로젝트 핵심 인공지능 모델
- 보행등의 색상을 분류하는 모델을 만들어 시각 장애인이 보행등을 구분할 수 있도록 도와준다.
- 보행등의 색상을 분류하는 모델을 만들기 위해 YOLOv8 모델을 사용하였다.
- 데이터셋은 직접 수집하였고, 총 2,200장의 이미지를 수집하였다. 그 중 더미 데이터를 제거하여 약 1,946장의 이미지가 최종적으로 사용되었다.
- 데이터셋은 보행등의 색상별로 나누어져 있으며, 각 색상별로 약 1000장의 이미지가 있다.
- Class는 'ltd_green', 'ltd_red' 두 가지로 나누어져 있다.

## 프로젝트 구조
- `dataset` : 데이터셋 관련 처리 코드
- `yolo` : 학습 및 테스트 관련 코드
- `install_packages.bat` : 필요한 패키지 설치 스크립트

##  NVIDIA CUDA INFO
* PyTorch: v1.7.1+cu110
* NVIDIA CUDA: v11.2
* NVIDIA cuDDN: v8.1.0 (January 26th, 2021)
  * Add environment variable 'CUDA\v11.2\bin' (PATH)
  * Add environment variable 'CUDA\v11.2\include' (PATH)
  * Add environment variable 'CUDA\v11.2\lib\x64' (PATH)

## 구동 방법
_(주의!, 해당 환경은 RTX 3060을 사용하는 환경을 기준으로 한다. CUDA 11.2 버전의 경우 문제가 없지만 CUDA 버전이 다른경우 `install_package.bat` 파일의 PyTorch 버전을 본인의 CUDA을 확인하여 변경하여야 한다.)_

- `Python 3.9`버전으로 가상환경을 만든다. 
- `install_packages.bat`을 실행하여 필요한 패키지를 설치한다.
- `yolo_config.yaml` 파일을 정의한다.
```yaml
path: "<데이터셋 ROOT 경로>"
train: "<(학습)데이터셋 폴더 경로 [ROOT 경로 생략]>"
val: "<(테스트)데이터셋 폴더 경로 [ROOT 경로 생략]>"

nc: 2
names: ["tld_green", "tld_red"]

# Hyperparameters -------------------------------------------------
translate: 0.1  # image translation (+/- fraction)
scale: 0.2  # image scale (+/- gain)
shear: 0.2  # image shear (+/- deg) from -0.5 to 0.5
perspective: 0.1  # image perspective (+/- fraction), range 0-0.001
flipud: 0.7  # image flip up-down (probability)
fliplr: 0.5  # image flip left-right (probability)
mosaic: 0.3  # image mosaic (probability)
mixup: 0.1  # image mixup (probability)
# -----------------------------------------------------------------
```
* `main.py` 파일에서 `yolo_train()` 함수의 주석을 해제하고 실행하면 학습이 진행된다.
* Data Augmentation을 적용하려면 `yolo_config.yaml` 파일의 Hyperparameters 부분을 수정한다.
  + Hyperparameters 는 `yolov8n.pt` 모델을 `원본`데이터로 학습한 후 다음과 같은 순서로 파라미터를 적용시켜 각각 따로 학습한다.
  + `translate` > `scale`
# 모델 성능
![model_train_result](/model_train_result.png)

# 개발자
- 한양대학교 ERICA 스마트융합공학부 소속 2023030137 최시훈 (스마트ICT융합 전공) [PM]
- 한양대학교 ERICA 스마트융합공학부 소속 2023063890 이정호 (스마트ICT융합 전공)
- 한양대학교 ERICA 스마트융합공학부 소속 2023015105 함서규 (스마트ICT융합 전공)

# 참고자료
* 논문
  - 시각장애인 길 안내 서비스를 위한 딥러닝 기반 횡단보도 가이드 솔루션 개발 _(김서현, 최인훈, 박수용, 정홍주, 홍승준, 허의남*
경희대학교)_

# LICENSE
BSD 2-Clause License

Copyright (c) 2023, CHOI SI-HUN

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
