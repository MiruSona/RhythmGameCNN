# RhythmGameCNN

## 프로젝트 설명
* 리듬게임 "Osu!"의 노트 파일을 합성곱 신경망에 학습시킨 후, 신경망이 생성한 노트와 원본 노트의 유사율을 구한 연구
* 가천대학교 게임공학 석사 졸업 논문 : [RISS링크](http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=88483685188c1d34ffe0bdc3ef48d419)

## 개발환경
* anaconda
* python
* keras

## 주요 기능
* AudioToSpectrogram : 오디오 파일을 Spectrogram 이미지로 변환시켜주는 파이썬 코드
* Keras : Spectrogram 이미지들을 학습 및 학습한 내용을 바탕으로 노트 생성
* AlexNet, DenseNet, GoogLeNet, ResNet 4개의 모델 사용 및 비교함