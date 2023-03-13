import csv
import random;
import string

# 이름 생성 함수들
def firstName():
    first = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", "안",
             "송", "류", "전", "홍", "고", "문", "양", "손", "배", "조", "백", "허", "유", "남", "심", "노", "정",
             "하", "곽", "성", "차", "주", "우", "구", "신", "임", "나", "전", "민", "유", "진", "지", "엄", "채",
             "원", "천", "방", "공", "강", "현", "함", "변", "염", "양", "변", "여", "추", "노", "도", "소", "신",
             "석", "선", "설", "마", "길", "주", "연", "방", "위", "표", "명", "기", "반", "왕", "금", "옥", "육",
             "인", "맹", "제", "모", "장", "남", "탁", "국", "여", "진", "어", "은", "편", "구", "용"]

    return random.choice(first)


def LastName():
    last =  ["가", "강", "건", "경", "고", "관", "광", "구", "규", "근", "기", "길", "나", "남", "노", "누", "다",
            "단", "달", "담", "대", "덕", "도", "동", "두", "라", "래", "로", "루", "리", "마", "만", "명", "무", "문", "미", "민", "바", "박",
            "백", "범", "별", "병", "보", "빛", "사", "산", "상", "새", "서", "석", "선", "설", "섭", "성", "세", "소", "솔", "수", "숙", "순",
            "숭", "슬", "승", "시", "신", "아", "안", "애", "엄", "여", "연", "영", "예", "오", "옥", "완", "요", "용", "우", "원", "월", "위",
            "유", "윤", "율", "으", "은", "의", "이", "익", "인", "일", "잎", "자", "잔", "장", "재", "전", "정", "제", "조", "종", "주", "준",
            "중", "지", "진", "찬", "창", "채", "천", "철", "초", "춘", "충", "치", "탐", "태", "택", "판", "하", "한", "해", "혁", "현", "형",
            "혜", "호", "홍", "화", "환", "회", "효", "훈", "휘", "희", "운", "모", "배", "부", "림", "봉", "혼", "황", "량", "린", "을", "비",
            "솜", "공", "면", "탁", "온", "디", "항", "후", "려", "균", "묵", "송", "욱", "휴", "언", "령", "섬", "들", "견", "추", "걸", "삼",
            "열", "웅", "분", "변", "양", "출", "타", "흥", "겸", "곤", "번", "식", "란", "더", "손", "술", "훔", "반", "빈", "실", "직", "흠",
            "흔", "악", "람", "뜸", "권", "복", "심", "헌", "엽", "학", "개", "롱", "평", "늘", "늬", "랑", "얀", "향", "울", "련"]

    return random.choice(last)


def address():
    f_Ad = open('build_seoul.txt', 'r')
    random_line = random.choice(list(f_Ad.readlines())).splitlines()[0]
    f_Ad.close()
    return random_line


def loginId():
    n = random.randrange(5,10)
    loginId = ""
    for x in range(n):
        loginId += str(random.choice(string.ascii_lowercase))

    return loginId


def password():
    lenNum = 64
    password = "";
    for y in range(64) :
        password += random.choice(password_make)

    return password


# ------------ main

password_make = string.ascii_letters + string.digits
create_cnt = 1000

f_Save = open('random_member.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f_Save)

for i in range(create_cnt) :
    name = firstName() + LastName() + LastName()
    address_full = address()
    address_list = address_full.split('|')

    login_Id = loginId()
    email = login_Id + "@google.com"

    sido = address_list[1]
    sigungu = address_list[2]
    eupmyeondong = address_list[3]
    street = address_list[9]
    zipcode = address_list[19]

    wr.writerow([sido, sigungu, eupmyeondong, street, zipcode, email, login_Id, name, password()])
    print([sido, sigungu, eupmyeondong, street, zipcode, email, login_Id, name, password()])

f_Save.close()