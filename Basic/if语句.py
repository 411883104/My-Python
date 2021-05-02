str='Hello'
test='hello'
for i in str:
    if i=="l":
        print(i)
    else:
        print("NO")

a=30
b=20
#多条件判断用and和or
if a==30 and b==20:
    print("Yes")
else:
    print("No")
if a==30 or b==10:
    print("YES")
else:
    print("NO")

if a==10:
    print(a)
elif a==20:
    print(a+10)
else:
    print(b)

list=[]
if list:
    print("NO empty")
else:
    print("empty")