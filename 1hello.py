print("Hello World!")
a = 3
b = 4
print(a+b)
print(type(a))
print(a*b)
#곱하기
print(a/b)
#나누기
print(a//b)
#몫
print(a%b)
#나머지
print(a**b)
#제곱


c = "python\'s favorite food is you"
#\ 표시로 따움표 구분
print(c)
string4 = 'python is good language \n for you'
print(string4)
#따움표 3개를 사용하면 쓴 문장 형식 그대로 나옴

string5 = """ { -- - - - -- - - --  }"""
print(string5)

#파이썬은 쉽게 인댁싱이 가능

print(string4[0])

#인덱싱 : 슬라이싱

print(string4[:8])
print(string4[8:])
print(string4[2:11:3])
print(string4[::-1])
#거꾸로 읽기
#이상:미만:간격(앞으로 뒤로)

s6 = "I eat %d apples." %3
print(s6)

number = 11
day = "three"

s7 = "I ate %d apples and I got sick for %s days" %(number,day)
print(s7)

s8 = "asdfasdf asdf {name} asdfasdf {age}".format(name = "정지훈",age = 11)
print(s8)

#소수점 자리 짜르기

s9 = "%.4f" %(10/3)
print(s9)

#문자 개수 카운트
print("a~z 중에서 문자 입력 : ")
anychar = "e"
s10 = "Hello World abcdefghijklmnop"
print("s10 문자열에서 %s의 문자 개수는 %d 입니다." %(anychar,s10.count(anychar)))
if (s10.find(anychar) == -1) :
    print("s10 문자열에는 찾는 문자가 없습니다.")
else :
    print("s10 문자열에서 %s 가 처음 등장하는 위치는 %s 자리입니다." %(anychar,s10.find(anychar)+1))


# 문자열 삽입

s11 = "안에 있는\n"
local_s11 = s11.join("abcd")
print(local_s11)

#대소문자 전환

s12 = "HELLO"
print(s12.lower())
s13 = "hello all lower"
print(s13.upper())

#특정 문자열 전환 : replace

s14 = "Life is full of somethings to do"
print(s14.replace("somethings to do","Happiness"))

print("\n")
#문자열 특정 문자로 자르기

s15 = "배 안의 사과 안의 씨앗 안의 DNA"
print(s15.split(" 안의 "))

local_s15 = s15.split()
print(local_s15)

numbers = [1,2,2,3,3,3]
numbers.remove(3)
print(numbers)

# 생각보다 어렵네;; 반복문 사용해서 "안의" 제거하기
print("생각보다 어렵네;; 반복문 사용해서 \"안의\" 제거하기")
# local_s 는 왜 있는걸까..되긴 되네
print("\n")
print("원래 표는 %s 입니다." %local_s15)
for i in local_s15 : 
    if (local_s15.count('안의') > 0) :
        local_s15.remove('안의')
        print(local_s15)
else : print("더 이상 값이 없음")

print(local_s15)


