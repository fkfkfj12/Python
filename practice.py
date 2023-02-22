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
#지하철 칸별로 10명, 20명, 30명
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

cabinet = {}