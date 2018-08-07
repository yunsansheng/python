# 基本语法
- return关键字只能用到函数中
- break 只能用在loop中
- 位置参数，关键词参数（给了初始值就是位置参数）
- 易混淆
	- / 除
	- //整除
	- % 取余
	- \ 这个不是运算法，是转义符
	- is 和 in
		- is（id,value,type）
		- in (exists or not)
#基本数据类型
- number （不可变）
	- int
	- float
	- complex
	- bool(继承自int)

- string （不可变）
- list （可变）
- tuple（不可变）
- set（可变）
- dictonary（可变）


```
常用的两种类型判断方法 
1. type()继承
2. isinstance() 可判断继承关系
type（1） => int
type(True) => bool

isinstance(True,int) => True

```


#数据结构比较
- list,tuple
- dict,set

|list|tuple|dict|set|
|---|:---:|---|---|
|[]|()|{key:value}|{}|
|可变|不可变|key不可变，不能重复|可变，排重|
|有序|有序|无序|无序|


- set可变，但是不能放入可变对象，比如 list或者其他的set
- 直接赋值{},将会是dict类型，如果要创建set类型，必须set{[]}
- 如果赋值{1,2,3},将是set类型
- set可以进行集合运算


# 常用函数
- open（）
	+  参数file
	+  参数mode（默认r）

- sorted(list,reverse=False)
- zip(seq1,seq2,...) =>[(),()]

# 高级用法
- 列表生成式
	- [i for i in range(1,11)]
	- same as 
	
		```
		def list_comprehension()
			lst=[]
			for i in range(1,11):
				lst.append(i)
			return lst
		```
	- 优势是性能快，简洁
- 字典生成式
	- {i:i+1 for i in range(4)}
	- 性能占优
