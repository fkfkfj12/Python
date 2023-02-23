# 
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 " +animal + "의 이름은" +name+"예요")
# print(name+"는 " +str(age)+ "살이며,"+ hobby+"을 아주 좋아해요")
# print(name+ "는 어른일까요? "+ str(is_adult))


# print(2**3) #2^3 = 8
# print(5%3) # 나머지 구하기 = 2
# print(10%3) # 1
# print(5//3) # 몫 구하기 = 1
# print(10//3) # 3

# print(abs(-5)) # 5 abs는 절대값
# print(pow(4,2)) # 4^2 =  4*4 = 16  pow 는 4를 2번 곱함
# print(max(5,12)) # 최댓값 12
# print(min(5,12)) # 최소값 5
# print(round(3.14)) # 반올림 3

# from math import *
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) # 올림. 4
# print(sqrt(16)) #제곱근. 4

# from random import *
# print(random()) #0.0~ 1.0 미만의 임의의 값 생성
# print(random()*10) #0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0~ 10 미만의 임의의 값 생성
# print(int(random()*10)) # 0~ 10 미만의 임의의 값 생성
# print(int(random()*10)) # 0~ 10 미만의 임의의 값 생성

# print(int(random() * 45 ) + 1) #1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randint(1,45)) #1 ~ 45 이하의 임의의 값 생성

# print(randint(4,28))

# jumin = "990120-1234567"
# print("성별 : " + jumin[7])  # 0부터 시작해서 계산
# print("연 : " + jumin[0:2]) # 0부터 2직전까지 = (0,1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리" + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터)" + jumin[-7:]) #맨뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower()) # 소문자로
# print(python.upper()) # 대문자로
# print(python[0].isupper()) # 0번째 값이 대문자가 맞냐? 맞으면 true
# print(len(python)) # 전체 문자열의 길이
# print(python.replace("Python", "Java")) # Python 을 Java로 변경하여 출력

# index = python.index("n") # n 을 찾음
# print(index)
# index = python.index("n", index +1) # 처음 찾았던 n 다음번에 있는 n 을 찾음
# print(index)

# print(python.find("Java"))  # Java가 없어서 -1 을 출력
# print(python.index("java"))  # Java가 없어서 오류가 생김

# print(python.count("n"))

# print("a" + "b")
# print("a" , "b")

# 방법 1
# print("나는 %d살 입니다." % 20) # d는 정수값
# print("나는 %s을 좋아해요." % "파이썬") # s는 문자열
# print("Apple 은 %c로 시작해요." %"A") # c는 문자 한글자만

# print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# 방법 3
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age = 20 , color="빨간"))

# 방법 4 (v3.6 이상부터 사용가능)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요.") # f를 쓰고 쓰면 실제 변수 값을 가져와서 출력

# print("백문이 불여일견 \n백견이 불여일타")  #\n 줄바꿈
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")  # \" , \' 는 문장내에서 따옴표를 쓸수있다
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장내에서 \ 로 쓰임

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rpine") 

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")


# url = "http://naver.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈 씨를 유재석씨 / 조세호씨 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list=[5,2,4,3,1]
# num_list.sort()
# print(num_list)
# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)
# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list=["조세호", 20, True]
# num_list=[5,2,4,3,1]
# print(mix_list)

# 배열 합치기
# num_list.extend(mix_list)
# print(num_list)

# cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))   #[] 일때 없는 값이면 프로그램 종료 .get() 일때 없는 값이면 None 출력후 프로그램 계속됨
# print(cabinet.get(5,"사용 가능"))  # 5가 없는 값일때 사용가능을 출력


# print(3 in cabinet)  #True
# print(5 in cabinet)  #False

# cabinet = {"A-3":"유재석","B-100":"김태호"}   # 키 값은 정수가 아닌 문자도 가능
# print(cabinet["A-3"])
# print(cabinet["B-100"])
# # 사전
# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 모든값 제거
# cabinet.clear()
# print(cabinet)


# # 튜플
# menu = ("돈까쓰","치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스")  튜플은 .add 불가능

# # name="김종국"
# # age=20
# # hobby = "코딩"
# # pritn(name, age, hobby)

# (name, age, hobby )= ("김종국", 20 , "코딩")
# print(name,age,hobby)

# # 집합 (set) , 중복 안됨, 순서 없음
# my_set= {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석","박명수"])
# #교집합 (java와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# #합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# #차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# # 자료구조의 변경
# # 커피숍
# menu= {"커피","쥬스", "우유"}
# print(menu,type(menu))

# menu = list(menu)
# print(menu,type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# menu = set(menu)
# print(menu,type(menu))

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성
# users = list(users) #users 의 타입을 list 로 변경

# shuffle(users)
# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

# print("-- 당첨자 발표 --\n 치킨 당첨자 : {0} \n 커피 당첨자 : {1}  \n -- 축하합니다 --".format(winners[0],winners[1:]))

# if

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":ㄴ
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10<= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0<= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for ( 반복문 )
# for waiting_no in range(1,5):  # 1,2,3,4
#     print("대기번호 : {0}" .format(waiting_no))

# starbucks = ["아이어맨", "토르" , "아이템 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요" .format(customer, index))
    index -= 1
    if index ==0:
        print("커피는 폐기처분되었습니다.")