
## 1月10日

### 学习python基本语法

- 分支语句
- 循环语句
- 变量类型
- 以决策系统为例进行锻炼学习

```python
a = input('1:')  
b = input('2:')  
c = input('3:')  
d = int(input('score:'))  
if (a=='通过') and (b=='通过'):  
    e=1  
else:  
    if (a=='通过') or (b=='通过'):  
        if ((a=='通过') and (c=='通过')) or ((b=='通过') and (c=='通过')):  
            e=1  
        else:  
             e=0  
    else:  
        e=0  
if (d>=60) and e:  
    print('pass')  
else:  
    print('not pass')
```

## 1月11日

### 学习列表、字典、元组和集合的相关知识

1. 列表：
	-  显示元素下标：`lst.index()`
	- 添加元素：
		- 末尾添加单个元素：`lst.append()`
		- 末尾添加多个元素：`lst.extend(lst2)`
	- 插入元素：`lst.insert(2,'nb')`（在下标为2的位置插入‘nb’）
	- 列表的切片：`lst[start:end:step]`
	- 删除元素：
		- 删除指定元素：`lst.remove()`
		- 删除指定下标元素：
			- `lst.pop()`
			- `del lst[]`
		- 删除一片元素：`lst[1:5]=[]`
	- 清空列表：`lst.clear()`
	- 列表元素的排序：
		- 不生成新列表：`lst.sort(reverse=False)`  ==(默认为False即升序，改为True则为降序)
		- 生成新列表：`lst2=sorted(lst,reverse=False)`   (reverse同上)
	- 列表生成式：`lst=[i*i for i in range(1,10) ]`
2. 字典：
	- 字典的创建：
		- `d1={'judy':18,'tony':34,'ruby':18}`
		- `d2=dict(name='jack',age=19)`
	- 字典元素的查询：
		- `age=d[]`
		- `age=d.get()`
	- 字典元素的增添：`d[未有的元素]=赋值`
	- 字典元素的修改：`d[已有的元素]=赋值`
	- 字典的删除：`del d[]`   ==(若加方括号则为删除指定键的元素，无方括号则为删除整个字典)
	- 字典视图的获取：
		- 键的获取：`d.keys()`
		- 值的获取：`d.values()`
		- 键值对的获取：`d.items()`
	- 字典表达式：`d={x:y for x,y in zip(lst1,lst2)}`
3. 元组：
	-  特征：==不可修改，为不可变对象
	- 元组的创建：
		- `t=(10,)`   ==(元组中只有一个元素时括号与逗号不能省略，多个时则可以省略)
		- `t=tuple(())`
	- 元组的遍历：与普通的遍历一样
4. 集合：
	- 集合的创建：
		- `s={10,20,30,'jack'}`
		- `s=set((1,13,45,'candy'))`
	- 集合元素的增添：
		- 增添单个：`s.add()`
		- 增添多个：`s.update(lst)`
	- 集合元素的删除：
		- 删除单个：`s.remove()`和`s.discard()`   ==(用remove删除的元素若不存在会报错，用discard则不会报错)
		- 随机删除：`s.pop()`
		- 清空：`s.clear()`
	- 集合的数学操作：
		- 并集：`s1 | s2`
		- 交集：`s1 & s2`
		- 差集：`s1 - s2`
		- 对称差集：`s1 ^ s2`
	- 集合生成式：`s={i for i in range(1,10)}`
5. 实操熟悉python语法：
```python
def judge(a):  
    sum=0  
    while a:  
       sum+=1  
       a//=10  
    return sum  
max=int(input('请输入最大数：'))  
num=0  
for i in range(100,max):  
    n=judge(i)  
    sum=0  
    a=0  
    for j in range(n):  
        k=i  
        while k:  
            a=k%10  
            sum+=int(a**n)  
            k//=10  
        if sum==i:  
            print(i,end='\t')  
            num+=1  
print()  
print('水仙花数的个数为：',num)
```

## 1月12日

### 字符串和错误捕捉结构的学习，初始类与对象

1. 字符串：
	- 查找：
		- 查找指定元素第一次出现时的下标：`str.find()`
		- 查找指定元素最后一次出现时的下标：`str.rfind()`
	- 大小写的转换：
		- 全转大写：`str.upper()`
		- 全传小写：`str.lower()`
		- 每个单词首字母大写，其余全转小写：`str.title()`
		- 首字母大写，其余全转小写：`str.capitalize()`
		- 大小写交换：`str.swapcase()`
	- 内容的对齐：
		- 左对齐：`str.ljust(所占位数，填充字符)`
		- 右对齐：`str.rjust(所占位数，填充字符)`
		- 居中对齐：`str.center(所占位数，填充字符)`
		- 补零右对齐：`str.zfill(所占位数，填充字符)`   ==(有负号时0补在负号后面)
	- 内容的劈分：
		- 左劈分：`str.split(劈分标志，劈分次数)`
		- 右劈分：`str.rsplit(劈分标志，劈分次数)`
		- 劈分时若不填写参数，则默认以==空格==为劈分标志，同时全劈完
	- 内容的替换和合并：
		- 替换：`str1=str.replace(指定内容，替换个数)`
		- 合并：`str1=str.join()`
	- 切片：与列表的切片操作一样
	- 格式化字符串：`print('我叫%s，今年%d岁，是%s' % (name,age,status))`
	- 编码与解码：
		- 编码：`code=str.encode(encoding='编码类型')`
		- 解码：`code.decode(encoding='编码类型')`   ==(此处code为上文的code)==
	- 获取字符串的内容：`eval()`     如：`eval('{1,2,3}')`={1,2,3}
2. 错误捕捉结构：
```python
import traceback  
#引入traceback模块  
try:  
    #试运行该块的代码  
    a=int(input())  
    b=int(input())  
    res=a/b  
except:  
    #如果try板块的代码出错，则运行该处代码  
    print('something wrong')  
    #打印错误信息  
    traceback.print_exc()  
else:  
    #如果try板块代码正常运行，则运行该处代码  
    print(res)  
finally:  
    #无论try代码出错与否，都会运行该处代码  
    print('over')
```
3. 类与对象的初始：
```python
class Student:  
    '''此处的self及后续的self均为创建的变量，如stu1和stu2  
       其后面的参数为self的内容，可在定义变量时设定  
       而__init__()这个函数就是用来设置self初始值的函数'''  
    def __init__(self,name,age,gender,born_place):  
        self.name=name  
        self.age=age  
        self.gender=gender  
        self.born_place=born_place  
    edit_num='123.456.789'  
  
    '''这个函数的用法跟普通函数大同小异，区别在于这个函数需要用“类名（即上面的Student）”.函数名（）来调用'''  
    def eat(self):  
        print('%s is eating' % self.name)  
  
    '''此处为静态方法，用法跟上面的函数类似，这个可以不用参数'''  
    @staticmethod  
    def sm(per1,per2):  
        print('%s is playing with %s' % (per1.name,per2.name))  
  
    '''此处为类方法，用法同上，不过这个必须有一个cls参数，这个cls即上面的clss Student'''  
    @classmethod  
    def cm(cls,person):  
        print('You are a %s' % cls.__name__)#此处的cls.__name__()是获取类名，即Student  
        print('%s is eating' % person.name)  
stu1=Student('Ruby',18,'woman','USA')  
stu2=Student('Kenvy',19,'man','UK')  
print(stu1.name)  
stu1.eat()  
Student.cm(stu1)  
Student.sm(stu1,stu2)  
print(Student.edit_num)  
'''------------动态绑定函数或参数-------------'''  
stu1.score=80#仅仅将score这一参数绑定在stu1上，不影响stu2  
print(stu1.score)  
def drink():  
    print('you are sb.')  
stu1.drink=drink  
stu1.drink()  
#stu2.drink()  drink绑定在stu1上，故stu2不能调用该函数
```

## 1月13日

### 进一步学习类与对象及文件的相关操作

1. 以决策系统为例学习类与对象：
```python
class Judge:  
    flag=0  
    def __init__(self,judge1,judge2,judge3):  
        self.judge1=judge1  
        self.judge2=judge2  
        self.judge3=judge3  
    def decide(self,judge1,judge2,judge3):  
        if self.judge1=='pass' and self.judge2=='pass':  
            self.flag=1  
        else:  
            if self.judge1=='pass' or self.judge2=='pass':  
                if ((self.judge1=='pass') and (self.judge3=='pass')) or ((self.judge2=='pass') and (self.judge3=='pass')):  
                    self.flag=1  
                else:  
                    self.flag=0  
            else:  
                self.flag=0  
class Aspect1(Judge):  
    def __init__(self,judge1,judge2,judge3,aspect1):  
        #super()为返回父类去寻找对应函数  
        super().__init__(judge1,judge2,judge3)  
        self.aspect1=aspect1  
    def decide(self,judge1,judge2,judge3,aspects1):  
        super().decide(judge1,judge2,judge3)  
        if self.flag and self.aspect1>=60:  
            print('pass')  
        else:  
            print('not pass')  
a=input('first judge:')  
b=input('second judge:')  
c=input('third judge:')  
d=int(input('the score:'))  
t=Aspect1(a,b,c,d)  
t.decide(a,b,c,d)
```
2. 文件相关操作的学习：
```python

#w为只写，r为只读，a为追加写入，+使模式变为读写；w写入的会覆盖原有的，a则是追加写入  
with open('D:/霜降2.png','rb') as image:  
    #以二进制下的只读方式打开D盘中一个名为霜降2的png文件，并将其起名为image  
    with open('copyimage1','wb') as copyimage:  
        #以二进制下的写入方式打开copyimage1，若没有则创建一个该文件，并将其起名为copyimage  
        copyimage.write(image.read())  
        #将image中读取到的内容写入copyimage，完成文件的复制  
  
#用with不用加上close语句，不用with则需要close语句来关闭文件  
fp=open('text.txt','a+')  
fp.write('nb')  
fp1=open('text.txt','r')  
c=fp1.read()  
print(c)  
fp.close()
```

## 1月14日

### 学习os与os.path模块

1. os模块
	- 打开记事本：`os.system('notepad.exe')`
	- 打开计算器：`os.system('calc.exe')`
	- 打开指定文件：`os.startfile('文件地址')`
	- 获取当前目录的地址：`os.getcwd()`
	- 获取指定文件的目录与信息：`os.listdir('文件')`
	- 在本目录下创建指定目录名的目录：`os.mkdir('目录')`
	- 在本目录下创建多级目录：`os.makedirs('目录/目录/···')`
	- 移除本目录下的指定目录：`os.rmdir('目录')`
	- 移除本目录下的指定多级目录：`os.removedirs('目录/目录/···')`
	- 将工作目录转为指定目录：`os.chdir('目录')`
	- `os.walk()`能遍历指定目录下的所有文件及子目录，例子如下：
```python
path=os.getcwd()  
lst_path=os.walk(path)  
for pathh,dir,file in lst_path:  
    for filename in file:  
        if '.py' in filename:  
            print(filename)
```
		该代码能获取当前目录下所有后缀为.py的文件
2. os.path模块
	- 获取指定文件的绝对地址：`os.path.abspath('文件')`
	- 判断指定文件是否存在：`os.path.exists('文件')`
	- 将目录和文件进行拼接：`os.path.join('','文件')`
	- 分开目录及文件：`os.path.split('地址')`
	- 分开文件名及后缀：`os.path.splitext('文件')`
	- 提取文件名：`os.path.basename('地址')`
	- 提取目录名：`os.path.dirname('地址')`
	- 判断是否为目录：`os.path.isdir('地址')`
3. 补充：`变量名.endwith('')`是用来判断该变量末尾是否为指定内容，如：
```python
a='python'  
if a.endswith('on'):  
    print(a)
```


## 1月15、16日

### 学习线代
## 1月17日

### 整理笔记

## 1月18日

### 三大库的学习

1. numpy
	- 数组：
		- 产生数组：`np.array()`
		- 产生全零/全一数组：`np.zeros(元素个数，dtype='数据类型')/np.ones(同上)`   ==(数据类型可不指定，但默认为浮点数)==
		- 将数组设为指定值：`arr.fill()`   (fill只能填充与原数组相同数据类型的数)
		- 转换数组数据类型：`arr.astype('数据类型')`
		- 生成整数序列：`np.arange(start,end,step)`   ==(不包括终点)==
		- 生成等差数列：`np.linspace(start,end,数的个数)`   ==(包括终点)==
		- 生成随机数：
			- 生成0到1的普通随机数：`np.random.rand(数的个数)`
			- 生成标准正态分布数：`np.random.randn(数的个数)`
			- 生成随机整数：`np.random.randint(start,end,数的个数)`
		- 查看数组中的数据类型：`arr.dtype()`
		- 查看数组形状：
			- `arr.shape()`
			- `shape(arr)`
			- `size(arr)`
		- 查看元素数目：`arr.size()`
		- 查看数组维度：`arr.ndim()`
		- 索引与切片：与列表一样
		- 多维数组：
			- 创建：可参照c的思路，举例：`np.array([[1,2,3],[2,3,4]])`
			- 索引与切片：与列表思路类似，举例：`arr[0,1]`指取出第一行第二列的元素，`arr[1:,2:]`指取出在第二行之后且在第三列之后的内容
		- ==数组切片后不会开辟新的内存，(列表会开辟新的内存)==,若想开辟，则需要用一个函数：`b=arr[1:].copy()`
		- 花式索引：
			- 特征：可以随意取出想要的一堆元素，返回的是原对象的复制
			- 一维花式索引：
				- 利用列表：`arr[lst]`   ==(列表中的数字即需要取出元素的索引)==
				- 利用布尔数组：`arr[mask]`   ==(mask中为true的位置即需取出元素的索引)==
			- 二维花式索引：
				- 直接指定目标索引，举例：`arr[[1,2,3],[2,3,4]]`
				- 