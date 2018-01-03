# -*- coding: utf-8 -*- 
'''
#打印显示
print('Hello World')
print('100+200+300=',100+200+300)
print("the quick brown fox","jumps over","the lazzy dog!")
name=raw_input("your name:")
print "hello",name
print '100+200+300 =',100+200+300
print "1024*768 =",1024*768
'''

'''
#用户输入
#print absolute value of a integer
a = input("please enter a integer:")
if a >= 0:
	print a
else:
	print -a
#raw_input和input的区别：
#raw_input把输入的一切类型都定义为字符类型
#input输入的是什么类型就是什么类型
'''

'''
age = input('Please enter your age:')
if age >= 18:
	print "adult"
else:
	print "teenager"
'''

'''
a = int(input('Please enter a integer:'))
print a
a = 'ABC'
print a
'''

'''
a = 123
b = 456.789
c = 'Hello World!'
d = 'Hello,\'Adan\''
e = r'Hello,"Bart"'
print a,b,c,d,e
'''

'''
#占位符然后用变量输入
name = u'刘伟兵'
print 'hello %s your cat is lose!' % name
print('%5d-%03d' % (30001, 1000))
print('%.2f' % 3.1415926)
for i in range(10):
	print "the number is %03d" %i
for x in range(10):
	print "the number is %s" %x
rate = 10
print "growth rate is %d%%" %rate
print u'Hello,{0}, 成绩提升了 {1:.2f}' .format(u'小明',17.125)
s1 = 72
s2 = 98
rate = (s2-s1)*100/s1
print u"恭喜小明，今年的成绩比去年提高了%d%%" %rate
'''

'''
#列表练习
List = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
print List[0][0]
print List[1][1]
print List[2][2]
'''

'''
#if语句
height = input("Please input the height of m:")
weight = input("please input the weight of gongjin:")
BMI  = weight/(height*height)
print BMI
if BMI > 32.0:
	print u'xiaoming is too fat!'
elif 28.0<=BMI<=32.0:
	print  u'xiaoming is fat!'
elif 25.0<=BMI<=28.0:
	print 'xiaoming is heavy!'
elif 18.5<=BMI<=25.0:
	print 'xiaoming is ok!'
else:
	print 'xiaoming is too light!'
'''
'''
#循环语句
sum = 0
for i in range(101):
	sum = sum + i
print sum

sum1 = 0 
i = 0
while i<=100:
	sum1 = sum1 + i
	i = i + 1
print sum1

List = ['bart','lisa','adam']
for name in List:
	print "Hello %s" %name

sum2 = 0
i = 0
while i <= 100:
	sum2 = sum2 + i 
	if sum2 > 2000:
		print i
		break
	else:
		i = i + 1
	
print sum2
sum3 = 0 
i = 0
while i <= 100:
	i = i + 1
	if i%2 == 0:
		sum3 = sum3 + i
	else:
		continue
print sum3
'''

'''
#dict and set
Dict = {"liuweibing":{"age":28,"salary":8000,"car":"none","height":174,"weight":80},"wangqifeng":{"age":28,"salary":7000,"car":"none","height":174,"weight":70}}
print Dict["liuweibing"]["car"]
print Dict["wangqifeng"]
for k,v in Dict["liuweibing"].items():
	print k,v
s1 = set([1,2,3])
s2 = {2,3,4}
sj = s1&s2
sb = s1|s2
print sj
print sb
#sk = {s1,s2}  #集合和字典一样，他的key是不可变的，所有这里会报错因为列表可变所以不能作为key
#print sk 
t1 = (1,2,3)
t2 = (3,4,5)
s = {t1,t2}  #元组不可变所以可以加到集合以及字典里面
print s  
d1 = {t1:"hello",t2:"World"}
print d1
'''

'''
#函数学习
t1 = (1,-2,3,9,-10,2)
l1 = [1,2,-9,10,4,5,10,2,9,7]
print max(t1)
print max(l1)
a = abs   #函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给函数起了一个别名
print a(10)
print a(-10)
n1 = 255
n2 = 1000
print hex(n1)
print hex(n2)
'''

'''
#函数定义
def my_abs(x):
	if x > 0:
		return x
	else:
		return -x
print my_abs(-10)

import math
def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print (x,y)
r = move(100,100,60,math.pi/6)
print r    #其实上面那个就是返回一个元祖，只不过是将元组第一个值给了x，第二个给了y

def quadratic(a,b,c):
	if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
		raise TypeError("Wront type")
	if a == 0:
		print "这不是一元二次方程"
	elif b*b-4*a*c < 0:
		print "此方程式无根"
	else:
		s1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
		s2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
		return (s1,s2)
print 'quadratic(2,3,1) =',quadratic(2,3,1)
print 'quadratic(1,3,-4) =',quadratic(1,3,-4)
if quadratic(2,3,1) != (-0.5, -1.0):
	print u"测试失败"
elif quadratic(1,3,-4) != (1.0, -4.0):
	print u"测试失败"
else:
	print u"测试成功"
'''

'''
#函数的参数
def power(x):
	return x*x
print power(99)
def powerm(x,n):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
print powerm(5,3)
def powerm1(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
print powerm1(5)
def enroll(name,gender,age=6,city="beijing"):
	print "name: ",name
	print "gender: ",gender
	print "age: ",age
	print "city: ",city
enroll("lisa","Female",7)
enroll("lucy","Female",city="shanghai")
#一是必选参数在前，默认参数在后
#有多个默认参数时，调用的时候，既可以按顺序提供默认参数
#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
#定义默认参数要牢记一点：默认参数必须指向不变对象！否则效果如下
def add_end(L=[]):
	L.append("END")
	return L
print add_end()	#第一次正常的输出结果为["END"]
print add_end()	#这次输出结果为["END","END"]  不符合需求了需改动如下：
def add_end1(L=None):
	if L is None:
		L = []
	L.append("END")
	return L
print add_end1()
print add_end1()


#可变参数
def cale(paragrams):
	sum = 0
	for i in paragrams:
		sum = sum+i*i
	return sum
#这就得必须传入一个列表或者元组等之类的类型了，如：
print cale([1,2,3,4])
#我们想直接传入(1,2,3,4)这样的不确定参数个数就可以用下面这种方法：
def cale1(*paragrams):
	sum = 0
	for i in paragrams:
		sum = sum+i*i
	return sum
print cale1(1,2,3,4)
List1 = [2,3,4,5]
print cale1(*List1) #可以将现有的列表直接当参数导入进去
print cale(List1)

def person(name,age,**kw):
	print "name:",name,"age:",age,"others:",kw

person("yangmi",28,breast="36")
Dict1 = {"breast":37,"pussy":"peny"}
person("yangmi",29,**Dict1)
def product(*par):
	s = 1
	for i in par:
		s = s*i
	return s
print product(5)
print product(5,6)
print product(5,6,7)
print product(5,6,7,9)
'''
'''
#递归函数
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
print fact(1)
print fact(5)
print fact(10)
#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
#利用递归函数实现汉诺塔
def move(n,a,b,c):
	if n == 1:     #如果只有1个，直接将他挪到c
		print a,"-->",c
	else:
		move(n-1,a,c,b) #将上面的n-1个，通过c挪到b上
		move(1,a,b,c)	#将剩下的那个挪到c上
		move(n-1,b,a,c)	#将b上的通过a全部挪到c
move(3,"A","B","C")
'''

'''
List1 = range(100)
#取前5个元素
def cut(n):
	List2 = []
	for i in range(n):
		List2.append(List1[i])
	return List2
print cut(5)
#其实python已经有非常简单的切片方法：
print List1[0:5]
#前10个数每隔2个取1个
print List1[0:10:2]
#字符串也可以切片
A = "I like yangmi\'s big breast!"
print A[7:]
B = " I am honest boy! "
print B[1:][:-1]
#定义一个函数可以去除首尾的空格
def trim(x):
	index = 0
	for i in x:
		if i == " ":
			index = index + 1
			continue
		else:
			nx = x[index:]
			a = 0
			if len(nx)>0:
				while nx[a-1] == " ":
					a = a-1
				nnx = nx[:len(nx)+a]
				return nnx
print trim("     Hello    ")
print len(trim("     Hello    "))
def trim1(x):
	if x == '':
		return x
	while x[:1] == " ":
		x = x[1:]
	while x[-1:] == " ":
		x = x[:-1]
	return x
print trim1("        World             ")
print len(trim1("        World             "))
			
'''
'''
#判断一个变量的类型：用isinstance就可以
A = 123
B = "456"
C = 7.89
print isinstance(A,int)   #得出True的结果
print isinstance(B,int)	  #得出False的结果
print isinstance(C,float)
#迭代,判断一个对象是否可迭代用collections模块的Iterable类型判断
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance(A,Iterable)
print isinstance(C,Iterable)
#基本可以得出整数和浮点数是无法被迭代的字符可以
#如果想要对list实现下标循环可以用python内置的enumerate函数
for i,value in enumerate(['A','B','C']):
	print i,value
for i,value in enumerate(['A','B','C'],1):  #还可以指定下标从多少开始
	print i,value
#使用迭代查找一个list中最小和最大值，并返回一个tuple
List = [2,-9,2,5,6]
List1 = []
def FindMinandMax(*par):
	if len(par) > 0:
		Max = par[0]
		Min = par[0]
		for i in par:
			if i <= Min:
				Min = i
			elif i >=Max:
				Max =i
		return (Min,Max)
	else:
		return (None,None)
print FindMinandMax(*List)	
print FindMinandMax(*List1)
'''
'''
#列表生成式，如果我们要创建一个[1*1,2*2,3*3,...,n*n]这种列表该怎么办：
def CreateList(n):
	List = []
	for i in range(n+1):
		List.append(i*i)
	return List
print CreateList(10)
#其实有更好的方法解决这个问题：
List1 = [x*x for x in range(11)]
print List1
#for 循环后面还可以加条件
List2 = [x*x for x in range(11) if x%2 ==0]
print List2
List3 = [x+y for x in "ABC" for y in "XYZ"]
print List3
import os
List4 = [d for d in os.listdir('.')] #查看当前目录下的所有文件
print List4
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print L2
'''
'''
#生成器 generator
#方法1：创建一个generator，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x*x for x in range(10)]
print type(L)  #我们可抑制直接打印出列表的每一个元素
G = (x*x for x in range(10))
print type(G)  #我们可以通过next()获取generator的下一个返回值
print next(G)
print next(G)
print next(G)  #每一次打印出来的都是不一样的,因为generator保存的是算法，每次需要调用才计算下一个值
#用next方法打印出每一个元素那太头疼了，我们可用for循环打出
for i in G:
	print i   #因为之前已经用了3次next，所以这个for循环是从第4个开始打印出来
#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print b
		a,b = b,a+b
		n = n + 1
fib(10)
#上面的函数和generator只有一步之遥，我们只需要把print换成yield就可以变成generator
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n + 1
g1 = fib(10)
print type(g1)  #这就是定义generator的另一种方法

def odd():
	print "step1"
	yield 1
	print "step2"
	yield 3
	print "step3"
	yield 5
g2 = odd()
for i in g2:
	print i
'''
'''
#杨辉3角方法一：
def triangles(x):
	n = 1
	if n == 1:
		yield [1]
	n = n+1
	if n == 2:
		yield [1, 1]
	L = [1, 1]
	n = n+1
	while n <=x:
		count = n - 2
		medium = [L[i]+L[i+1] for i in range(count)]
		new_L = [1]
		new_L += medium
		new_L.append(1)
		yield new_L
		n = n+1
		L = new_L
g = triangles(10)
for i in g:
	print i
#杨辉3角方法二：
def triangles1():
    a=[1]
    while True:
        temp=a[:]
        yield temp
        a=[temp[i]+temp[i-1] for i in range(len(temp)) if i!=0]
        a.append(1)
        a.insert(0,1)

n = 0
results = []
for t in triangles1():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

#凡是可作用于for循环的对象都是Iterable类型；(可迭代对象)
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；（迭代器）
#集合数据类型如list、dict、str等是Iterable但不是Iterator，
#不过可以通过iter()函数获得一个Iterator对象。
#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1,2,3,4,5]:
	pass
#等价于
it = iter([1,2,3,4,5])
while True:
	try:
		x = next(it)
	except StopIteration:
		break
'''

#高阶函数
def add(x,y,f):
	return f(x)+f(y)
print add(-5,6,abs)
def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7])
print r
r1 = [x*x for x in [1,2,3,4,5,6,7]]
print r1