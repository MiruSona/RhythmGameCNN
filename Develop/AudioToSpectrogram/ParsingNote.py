
# coding: utf-8

# In[3]:


import os

#디렉토리 생성
def MakeDirectory(dir_path):
    try:
        if not(os.path.isdir(dir_path)):
            os.makedirs(os.path.join(dir_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

#Output 디렉토리 생성
def MakeOutputDir(dir_path):
    MakeDirectory(dir_path)
    MakeDirectory(dir_path + "/N")
    MakeDirectory(dir_path + "/A")
    MakeDirectory(dir_path + "/B")
    MakeDirectory(dir_path + "/C")
    MakeDirectory(dir_path + "/D")
    MakeDirectory(dir_path + "/AB")
    MakeDirectory(dir_path + "/AC")
    MakeDirectory(dir_path + "/AD")
    MakeDirectory(dir_path + "/BC")
    MakeDirectory(dir_path + "/BD")
    MakeDirectory(dir_path + "/CD")
    MakeDirectory(dir_path + "/ABC")
    MakeDirectory(dir_path + "/ABD")
    MakeDirectory(dir_path + "/ACD")
    MakeDirectory(dir_path + "/BCD")
    MakeDirectory(dir_path + "/ABCD")

#Text 파일 읽기
def ReadTextFile(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()
    return lines

#타이밍값 계산
#1000분의 1초로 만듬 -> 소수점 둘째자리에서 반올림 -> 10을 곱해서 양수만듬
#-> int로 변환해서 소수점 없앰
#4자리로 제한(빈칸은 0으로 채움)
def CalculateTiming(value):
    timing = float(value) / 1000.0
    timing = int(round(timing, 1) * 10)
    return str(timing).zfill(4)

#노트 위치 반환
def FindNotePosition(value):
    if value == "64":
        return "A"
    elif value == "192":
        return "B"
    elif value == "320":
        return "C"
    elif value == "448":
        return "D"
    else:
        return "N"

#롱 노트인지 체크
def CheckLongNote(value):
    if value == "128":
        return True
    else:
        return False
    
#Dictionary에 파싱한 노트 위치값 저장
def AddNotePos(dictionary, timing, note_pos):
    #이미 타이밍값이 있는지 체크 - 있을 경우 동시 노트
    if timing in dictionary:
        origin = dictionary[timing]
        # N 노트인지 체크 - 맞으면 그냥 넣음(기존 노트에 + 안함)
        if note_pos == "N" or origin == "N":
            dictionary[timing] = note_pos
        #이미 있는 노트인지 체크
        elif not note_pos in origin:
            new_value = "".join([origin, note_pos])
            sorted_value = "".join(sorted(new_value))
            dictionary[timing] = sorted_value
    #없을 경우 - 없는 노트
    else:
        dictionary[timing] = note_pos

#롱노트 자르기 - 저장할 dic / 시작타이밍 / 끝타이밍 / 저장할 노트 위치
def SliceLongNote(dictionary, start_timing, end_timing, note_pos):
    #길이 구하기
    length = int(end_timing) - int(start_timing)
    
    #길이가 0이 아니면
    if length != 0:
        #시작 타이밍 ~ 끝타이밍 까지 0.1초씩 같은 노트로 저장
        for index in range(0, length + 1):
            calc_timing = str(int(start_timing) + index).zfill(4)
            AddNotePos(dictionary, calc_timing, note_pos)
    #길이가 0이면 그냥 저장
    else:
        AddNotePos(dictionary, start_timing, note_pos)

#파싱
#필요한건 0, 2, 3, 5 인덱스
# 0 = 노트위치 / 2 = 타이밍 / 3 = 노트종류 / 5 = 롱노트일 경우 어디까지인지
# 노트위치 표시 = A,B,C,D로
# 안나온 노트 = N
# 동시노트 = AB, AC 요런식으로 붙음
# 롱노트는 잘라서 0.1초 단위로 같은 노트 포지션으로 파싱
def ParsingNoteFile(path):
    #텍스트 읽기
    read_text = ReadTextFile(path)
    #데이터 저장할 dictionary
    parsing_result = dict()

    #Text 읽고 파싱
    for read_line in read_text:
        #구분자로 나누기
        split_txt = read_line.split(',')
        #타이밍값
        timing =  CalculateTiming(split_txt[2])
        #노트 위치값
        note_pos = FindNotePosition(split_txt[0])
        #롱노트 인지 확인
        long_note = CheckLongNote(split_txt[3])
        
        #롱노트 아니면 그냥 추가
        if long_note == False:
            AddNotePos(parsing_result, timing, note_pos)
        #롱노트 일경우
        else:
            end_timing = CalculateTiming(split_txt[5].split(':')[0])
            SliceLongNote(parsing_result, timing, end_timing, note_pos)
    
    return parsing_result

#사용 예시
#result = ParsingNoteFile("./DreamCatcher_note_easy.txt")
#print(result.items())

