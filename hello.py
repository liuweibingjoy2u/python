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
'''
#高阶函数
def add(x,y,f):
	return f(x)+f(y)
print add(-5,6,abs)
def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7])
print type(r)
print r
r1 = [x*x for x in [1,2,3,4,5,6,7]]
print type(r1)
print r1
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
from functools import reduce
def fn(x,y):
	return x*10+y
print reduce(fn,[1,2,3,4,5])
def char2num(s):
	return digits[s]
print reduce(fn,map(char2num,'13579'))	#结合reduce和map将一个字符串转变成整数
#当然python有这个功能函数int轻松可以做到
print int('123456') #我们只不过是自己写了个转换成整数的函数
def int2(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return digits[s]
	return reduce(fn,map(char2num,s))
S = "12345678"
A = int2(S)
print type(A)
print A
#用lambda可以简化一点
def char2num(s):
	return digits[s]
def int3(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))
B = int3(S)
print type(B)
print B
'''
'''
print 'ABC'.lower()
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
	S = name[0].upper()
	H = name[1:].lower()
	return S+H
List = ['adam', 'LISA', 'barT']
print map(normalize,List)
#请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
	def redu(x,y):
		return x*y
	return reduce(redu,L)
print '3*5*7*9 =',prod([3,5,7,9])
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}
#方法一：这是自己捣鼓出来的
def str2flost(s):
	def fn(x,y):
		return x*10+y
	def fn3(l):
		n = 1
		sum = 0
		for i in l:
			x = i*10**-n
			n = n+1
			sum = sum+x
		return sum
	def str2num(s):
		return digits[s]
	index = s.find(".")
	zhengshus = s[0:index]
	xiaoshus = s[index+1:]
	zhengshu = reduce(fn,map(str2num,zhengshus))
	xiaoshu = fn3(map(str2num,xiaoshus))
	return zhengshu+xiaoshu
A=str2flost("123.456")
print type(A)
print A
#方法二：看别人搞得
def str2floast(s):
	def str2num(i):
		return digits[i]
	def fn(x,y):
		return x*10+y
	l = s.split(".")
	n = len(l[1])
	zhengshu = reduce(fn,map(str2num,l[0]))
	xiaoshu = reduce(fn,map(str2num,l[1]))
	return zhengshu+xiaoshu*10**-n
B = str2floast("1234.56789")
print type(B)
print B
'''
'''
#filter()函数用于过滤序列
def is_odd(n):
	return n % 2 == 1
print map(is_odd,[1,2,3,4,5,6,])		#这两个例子即可看出他们之间的区别，map是将返回值加入新列表
print filter(is_odd,[1,2,3,4,5,6])		#filter是将返回值为真的加入新列表
A=" I am   boy !   "
print len(A)
print A.strip()   #它只是删除字符头尾的空白
print len(A.strip(" "))
def notempty(s):
	return s and s.strip()
print filter(notempty,"I am boy ! ")    #这种方法就可以把所有的空白都删掉
print filter(notempty,["","I am",None,"boy"," ","!",])
'''
'''
#用filter求素数
def CreatNum():
	n = 1
	while True:
		n = n + 2
		yield n
def ZhiShu(n):
	return lambda x: x % n > 0
def primes():
	yield 2
	it = CreatNum()
	while True:
		n = next(it)
		yield n
		it = filter(ZhiShu(n),it)
for n in primes():
	if n < 1000:
		print n
	else:
		break
#方法二
import math
def getPrime(maxNum):
    primeList = []
    for x in range(2,maxNum+1):
        x_sqrt = math.sqrt(x)
        for prime in primeList:
            if prime > x_sqrt:
                primeList.append(x)
                break
            if x%prime==0:
                break
        else:
            primeList.append(x)
    return primeList
print getPrime(1000)
#方法3
def prime(x):  
    for i in range(2,x):  
        if x%i==0:  
            return False  
        if i==x-1:  
            return True  
output=filter(prime,range(2,10)) 
print output
'''
'''
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
	s = str(n)
	if s == s[::-1]:
		return True
	else:
		return False
print filter(is_palindrome,range(1000))
#字符串反转的多种方法：
A = "Hello World"
#方法一：
def fz1(s):
	return s[::-1]
print fz1(A)
#方法二:
def fz2(s):
	l = list(s)
	l.reverse()
	
	str = ''
	for i in l:
		str = str+i
	return str
#这4行可以用下面的方法代替
	return ''.join(l)
print fz2(A)
#方法3
from functools import reduce
def fz3(s):
	l = list(s)
	return reduce(lambda x,y:y+x ,l)
print fz3(A)

'''	
'''	
#排序算法
l = [1,-9,23,-46,29]
print sorted(l)
print sorted(l,key=abs)  #sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
l1 = ['bob', 'about', 'Zoo', 'Credit']
print sorted(l1,key=str.lower)  #忽略大小写排序
print sorted(l1,key=str.lower,reverse=True) #反转排序后的结果
l2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(list):
	return sorted(list,key=lambda x:x[0])  #key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print by_name(l2)
def by_score(list):
	return sorted(list,key=lambda x:x[1])
print by_score(l2)
#匿名函数lambda
f = lambda x,y,z:x+y+x   #lambda只是一个表达式，函数体比def简单很多。
print f(1,2,3)
def action(x):			
	return lambda y:x+y	 #这个函数返回了一个lambda的表达式
a = action(22)			 #这个a现在就成了一个函数等价于a = lambda y:22+y
print a(3)				 #这个就是把3作为y，然后通过a函数计算出结果25
#这里定义了一个action函数，返回了一个lambda表达式。
#其中lambda表达式获取到了上层def作用域的变量名x的值。
#a是action函数的返回值，a(22)，即是调用了action返回的lambda表达式。
'''	
'''	
#函数作为返回值，闭包
def lazy_sum(*args):
	def sum():
		s = 0
		for i in args:
			s = s + i
		return s
	return sum
l = [1,2,3,4,5]
print lazy_sum(*l)#这是一个求和函数，我们需要结果时需要再执行
print lazy_sum(*l)()
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(*l)
f2 = lazy_sum(*l)  #这两个函数是不同的函数
print f1 != f2     #从结果可知这两个不是等价的但是他们的值是相同的
print f1() == f2()
def count():
	fs = []
	for i in range(1,4):
		fs.append(i*i)
	return fs
print count()   #这种是直接返回一个列表，里面是我们需要的结果

def count1():
	fs = []
	for i in range(1,4):
		def fun():
			return i*i
		fs.append(fun)
	return fs
print count1()	#这种是返回一个列表里面都是函数，需要再次执行才能得出我们的结果
print count1()[0](),count1()[1](),count1()[2]() #看结果知道都是9，这是因为在返回函数的时候i的值都循环成了3

def count2():
	fs = []	
	def fun1(j):
		def fun2():
			return j*j
		return fun2
	for i in range(1,4):
		fs.append(fun1(i))
	return fs
print count2()[0](),count2()[1](),count2()[2]() #看结果可以知道这是我们需要的结果，这是因为我们加了一个函数，fun1把i的值固定了，所以才能得出想要的结果


#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def CreateCouter():
	def CreateNum():
		n = 1
		yield n
		while True:
			n = n+1
			yield n
	it = CreateNum()
	def counter():		
		return next(it)
	return counter
counterA = CreateCouter()
counterB = CreateCouter()
print counterA(),counterA(),counterA(),counterA(),counterA()
print counterB(),counterB(),counterB(),counterB()
'''		
'''
print filter(lambda x:x%2==1,range(1,20))
f = lambda x:x%2==1
print filter(f,range(1,20))
'''
'''
#装饰器
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
	def wrapper(*args,**kw):
		print 'call %s()' %func.__name__
		return func(*args,**kw)
	return wrapper
@log
def now():
	print "2018-01-04"
f = now
f()
print f.__name__  #可以看到结果是wrapper，而不是原先的now,这就可能导致一些依赖函数签名的代码执行错误，所以我们就可以用functools.wraps来做到保存原有的函数名：所以一个完整的decorator写法如下：
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper
#如果装饰器也要带参数，写法如下:
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s()' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log("execute")
def fun1(name,age):
	print 'my name is %s,i\'m %s' %(name,age)
fun1("liuweibing",28)
'''
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools,time
def metric(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		t = time.time()
		t1 = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(t))
		print '%s start executed in %s' %(func.__name__,t1)
		rs = func(*args,**kw)
		print '%s end executed in %s,it execute %s ms' %(func.__name__,time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime()),time.time()-t)
		return rs
	return wrapper
@metric
def fast(x, y):
    time.sleep(1)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(1)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print u'测试失败!'
elif s != 7986: 
    print u'测试失败!'
else:
	print u'测试成功'



