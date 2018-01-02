# -*- coding: utf-8 -*- 
'''
print('Hello World')
print('100+200+300=',100+200+300)
print("the quick brown fox","jumps over","the lazzy dog!")
name=raw_input("your name:")
print "hello",name
print '100+200+300 =',100+200+300
print "1024*768 =",1024*768
'''

'''
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
List = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
print List[0][0]
print List[1][1]
print List[2][2]
