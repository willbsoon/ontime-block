# 온타임 무력화 프로그램

## 1. 개발 목적

20분동안 자리를 비우면 자리비움 사유를 입력해야하는 온타임 프로그램을 무력화 하기위해 준비한 프로그램  

## 2. 사용법

```
pip install pyautogui
pip install windows-curses
```

```
python ./screenblock.py
```


## 3. 배포
exe 파일로 만들어 배포가능
but 아나콘다가 아닌 순수 파이썬으로 해야 용량을 줄일수 있음.

```
[파이썬 설치 폴더]>.\python -m venv .\newEnv
[파이썬 설치 폴더]>.\newEnv\Scripts\activate
```
새로운 가상환경을 만들었으면 라이브러리를 다시 받아야함

```
pip install pyautogui
pip install windows-curses
pip install pyinstaller           # 배포를 위해
```

그리고 아래와 같이 치면 됨.

```
pyinstaller -F screenblock.py    # -F 한파일로 만들기 위함
```


windows에서 win + R 눌러서 시작프로그램에 등록할 수 있음  
`shell:startup` 입력하면 폴더가 열림  
파일 복사해서 넣으면 시작프로그램에 등록 됨.

