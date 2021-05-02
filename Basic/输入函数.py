'''
#输入函数input()
str="hello"
str+="\nworld"
s=input(str)
#数值输入用int()
a=int(input())
print(a)
'''

#一行输入多个数
a,b=map(int,input().strip().split())
print(a,b)