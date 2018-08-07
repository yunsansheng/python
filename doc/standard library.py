enumerate #枚举
lambda
property


@classmethod
第一个传入类,cls（不需要穿入self）能直接调用类的属性和方法
@staticmethod
不需要传入self和类



tuple是有序集合，而set 和fozenset是无序集合


round函数，不是真正意义上的四舍五入
#1.Round(1.5) =2   Round(2.5)也等于2,这是因为Python3更改了特性，向偶数取整。
#2.The behavior of round() for floats can be surprising: 
#for example, round(2.675, 2) gives 2.67instead of the expected 2.68. 
#This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.


sort是数组的排序，sorted是针对所有可迭代对象的排序


x//y  floored quotient of x and y( he result is always rounded towards minus infinity:)  取整
#1//2 is 0, (-1)//2 is -1, 1//(-2) is -1, and (-1)//(-2) is 0.
x%y   remainder of x / y
divmod :Return the tuple (x//y, x%y)
x** y  x的 y次幂

math.ceil "Return the ceiling of x as an Integral."
math.floor "the floor of x as an Integral."	math.trunc(-1.5)= -2
math.trunc "Truncates x to the nearest Integral toward 0 " math.trunc(-1.5)= -1


#math 和cmath模块
#第一个模块允许您访问实数的双曲线，三角函数和对数函数，而后者允许您使用复数。


#按位运算符是把数字看作二进制来进行计算的,只能对整数进行运算
#Bitwise operations only make sense for integers.
#包括 &　｜　＾　~ << >>






