''' #튜플()값고정 / 리스트[]수정가능
a=list(1,2,3)
a=[]
a.append(a))
a=1,2,3  #튜플
a=list(a) #가능
a=list(1,2,3) #불가능
print(type(a))
'''

#set
a=[1,2,3,1,2,3] 저장가능
a=set({1,2,3,1,2,3}) 중복값없어짐
print(a)

a=set(b)
print(b)->{1,2,3}
print(*a)->1,2,3 #언패킹


c={1,2,3}    #87p
print(len(c))->3

#in 포함
if 2 in c:
    print("2있음")
else:
    print("x")

d=int(input()) #입력
if d in c:
    print("2있음")
else:
    print("x")

#딕셔너리
d={"one":1,"two":2."three":3}
print(d["one"])
print(d["four"]) #오류
#get은 특정 키에 해당하는 값을 가져올때 사용
print(d.get("four", "해당키가 없습니다."))
#get() 개수를 카운트 사용->중요


list=['a','b','c','d','c','b']
count={} #딕셔너리
#set / b=set() b=[]

for i in list:
    count[i]=count.get(i,0)+1

print(count)
    #중요한거

#key, value 출력 items
for key, value in count.items():
    print(key, ":", value)

#key만 출력 keys
print(count.keys())

#value만 출력 values
print(*count.values())


#문자로 형변환 str()
#%d 정수, %c 문자, %s 문자열
name='홍길동'
age=21
print('제 이름은 %s입니다.'%name)
print('제 이름은 %s입니다. 저는 %s살입니다.' %(name, age))
#f-string 활용
print(f"제 이름은 {name}입니다. 저는 {age}살입니다.")
#format() 활용
print("제 이름은 {}입니다. 저는 {}살입니다.").format(name,age))
#format() 번호
print("제 이름은 {1}입니다. 저는 {0}살입니다.").format(name,age))
