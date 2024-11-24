# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 보여줌
print(python.upper()) # 모두 대문자로 보여줌
print(python[0].isupper()) # 해당 변수의 첫번째 문자가 대문자인지 확인
print(len(python)) # 변수 문자의 전체 길이를 반환
print(python.replace("Python", "Java")) # replace("찾고 싶은 문자", "바꾸고 싶은 문자")

index = python.index("n") # python 변수에서 "n"이라는 글자가 몇 번째에 위치해있는지 알려줌
print(index)
index = python.index("n", index + 1) # index("n", 시작 위치) 해당 문자를 찾는 시작 위치를 추가로 적음으로써 해당 index 이후에 해당되는 문자를 찾을 수 있다.
print(index)

print(python.find("n")) # index와 비슷한 함수
print(python.find("Java")) # 내가 원하는 값이 해당 변수에 없을 경우 -1을 반환. index의 경우에는 오류가 뜸. 둘의 차이 알기.

print(python.count("n")) # 변수에서 해당 문자가 몇 번 반복되는지 계산해줌

# 문자열 포맷
print("a" + "b") # 문자열이 바로 합쳐짐
print("a", "b") # 띄어쓰기를 포함해 문자열이 합쳐짐

# 방법 1
print("나는 %d살입니다." % 20)  # % 뒤의 값을 문장 안의 %d에 넣겠다는 의미가 됨. d는 정수값만 의미함에 유의.
print("나는 %s를 좋아해요." % "파이썬") #  % 뒤의 문자열 값을 %s에 넣겠다는 의미.
print("Apple은 %c로 시작해요." % "A") # %c 는 character를 의미해서 한 글자만 받겠다는 의미.
# 참고로 %s 로만 쓰면 정수건 한 글자이건 상관없이 모두 다 출력 가능하다.
print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러 가지의 값을 적을 때는 괄호로 묶어서 표기해준다.

# 방법2
print("나는 {}살입니다." .format(30)) # .format() 괄호 안의 숫자가 {}안에 들어가게 됨.
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {2}색을 좋아해요." .format("파란", "빨간", "초록")) # format 안에 내용이 여러개 일 때 원하는 내용을 골라서 지정 가능하다.

# 방법 3
print("나는 {age}살이며, {colour}색을 좋아해요.".format(age = 20, colour = "빨간")) # format 안에 변수 선언을 할 수 있다.

# 방법 4 (v3.6 이상~)
age = 30
colour = "빨간"
print(f"나는 {age}살이며, {colour}색을 좋아해요.") # f"" 형식에 맞춰 "" 안에 문자를 써주면 실제 변수 값을 가져다가 활용할 수 있다.