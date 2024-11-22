# 애완동물을 소개해 주세요~
animal = "강이지"
name = "하루"
age = 11
like = "낮잠"
is_adult = age >= 3

'''
이렇게 하면 여러 문장이 
주석
처리가 됩니다.'''

print("우리집 " + animal + "의 이름은 " + name + "입니다")
# print(name + "는 "+ str(age) +"살이며, "+ like +"를 좋아해요")
print(name, "는 ", age, "살이며, ", like, "를 좋아해요")
print(name +"는 어른일까요? " + str(is_adult))

print(2**3) # 2^3 2의 3제곱이 됨
print(5%3) # 나머지 구하기. 2
print(10%3) # 1

print(5//3) # 몫 구하기. 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

