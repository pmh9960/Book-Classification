# Book Classification

## What we do

1. Slader의 책 표지들을 가져온다.
2. 책 표지들의 대분류에 의해 다음과 같이 분류한다.
   라벨 | Slader 대분류 | 폴더 명|
   :---:|:---:|:---:|
   0 | Foreign Languages | `foreign_languages`|
   1 | Literature and English | `literature`|
   2 | Science | `science`|
   3 | Social Sciences |`social_sciences`|
3. Superviesed Learning 으로 학습한다.
4. 다른 전공책 사진을 넣어 대분류를 예측한다.

## Install Requirement

```
- numpy
- h5py
- matplotlib
- tensorflow<1.6
- keras==2.1.5
```

### (Optional)

1. Preprocess

```- requests
- scipy==1.1.0
  - 전처리 할 때는 1.1.0
  - tensorflow 사용할 때는 1.4이상.
- beautifulsoup4
- pillow
```

2. Model visualization

```
- ipython[all]
- pydot==1.2.3
- pydot-ng
- graphviz
  - Windows에서는 pip으로 설치가 제대로 안됨.<br> 따로 찾아가서 설치할 것.
  - [Graphviz](https://www.graphviz.org/)
```
