
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

### 三大库中numpy的学习


1. 数组：
	- 产生数组：`np.array()`   ==(数组元素类型需相同)==
	- 产生全零/全一数组：`np.zeros(元素个数，dtype='数据类型')/np.ones(同上)`   ==(数据类型可不指定，但默认为浮点数)==
	- 将数组设为指定值：`arr.fill()`   (fill只能填充与原数组相同数据类型的数)
	- 转换数组数据类型：
		- `arr.astype(数据类型)`   ==(生成一个新数组)==
		- `np.asarray(arr,dtype=数据类型)`   ==(直接对原数组进行修改)==
	- 生成整数序列：`np.arange(start,end,step)`   ==(不包括终点)==
	- 生成等差数列：`np.linspace(start,end,数的个数)`   ==(包括终点)==
	- 生成随机数：
		- 生成0到1的普通随机数：`np.random.rand(数的个数/维度1，维度2，···)`
		- 生成标准正态分布数：`np.random.randn(数的个数/维度1，维度2，···)`
		- 生成随机整数：`np.random.randint(start,end,数的个数/size=(维度1，维度2，···))`
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
			- 利用布尔数组，跟一维数组类似
	- 返回非零位置的索引：`np.where(数组表达式)`
	- 数组排序：
		- 升序排列：`np.sort(arr)`   ==(生成新数组)==
		- 返回升序排列的索引：`np.argsort(arr)`
	- 数组元素求和：
		- `np.sum(arr)`
		- `arr.sum()`
	- 最大值/最小值/均值/标准差：
		- `np.max/min/mean/std(arr)`
		- `arr.max/min/mean/std()`
	- 相关系数矩阵：`np.cov(arr1,arr2)`
	- 转置(生成新数组)：
		- `arr.T`
		- `arr.transpose()`
	- 数组连接：
		- 横向连接：`np.hstack((arr1,arr2))`
		- 纵向连接：`np.vstack((arr1,arr2))`
		- 连接成三维数组：`np.dstack((arr1,arr2))`
	- 内置计算函数：
		- 绝对值：`np.abs(arr)`
		- 指数：`np.exp(arr)`
		- 中值：`np.median(arr)`
		- 累计和：`np.cumsum(arr)`



## 1月19日

### 三大库中pandas的学习

1. Series结构：
	- 特征：可以存放不同数据类型的元素
	- 创建：与numpy类似，`pd.Series(lst,index=)`   ==(可以用index指定下标，若不指定，则默认为跟列表一样的下标，同时series在赋值时可以用np.nan来赋空值)==
	- 查询索引：`arr.index`
	- 查询数值：`arr.values`
	- 索引与切片：与数组相同
	- 设置索引表头：`arr.index.name=''`
	- 改变索引值：`arr.index=list('')`   ==(当索引值被改变时，切片操作会包含终点)==![[Pasted image 20230119120505.png]]
2. DataFrame结构：
	- 特征：是个二维的表格，要求每一列数据类型相同，本质上是Series结构的二维展开
	- 创建：`pd.DataFrame(lst,index=,columns=)`   ==(index指定行索引，columns指定列索引)==
	- ==注：除了传入列表，也可以传入字典，字典的key代表列索引，value代表下面的值==
	- ![[Pasted image 20230119115800.png]]
	- ![[Pasted image 20230119115834.png]]
	- ![[Pasted image 20230119125244.png]]
	- 
	- 
3. 构造时间序列：`pd.date_range('起始日期',periods=跨度)`![[Pasted image 20230119121215.png]]
4.  查看数据：
	- 每一列的数据类型：`arr.dtypes`
	- 头尾数据：`arr.head()/tail()`   ==(不指定参数则默认为5)==
	- 行标：`arr.index`
	- 列标：`arr.columns`
	- 值：`arr.values`
5. 对数据的操作：
	- 读取excel的数据：`pd.read_excel('路径')`   ==(后面还可传入一个sheet_name参数，表示读取的工作表名，若无指定则默认为读取全部工作表)==
	- 行操作：
		- 行查询：
			- `arr.iloc[]`   ==(单行查询传入单个参数，多行查询利用切片方式)==
			- `arr.loc[]`   ==(同上，不过这个的切片包含终点)==
		- 添加一行：`arr=arr.append()`   ==(传入的参数需为series类型，且列数需相同)==
		- 删除一行：`arr=arr.drop([行索引1，行索引2，···])`
		- 对一行的数据进行求和：`arr.sum(axis=1)`   ==(axis默认为0，即纵向相加，改为1后可以对横向的数据进行求和)==
	- 列操作：
		- 列查询：
			- 查询列索引：`arr.columns()`
			- 查询列值：`arr['列索引1','列索引2',···]`   ==(后面还可以加个[start,end]来限定查询的列数)==
		- 增加一列：`arr['']=`
		- 删除一列：`arr=arr.drop('',axis=1)`   ==(axis是指定删除方向，默认为0，即横向删除，改为1则为纵向删除)==
	- 通过标签查询数据：`arr.loc[[行标1，行标2，···],[列标1，列标2，···]]`
	- 条件选择：`arr[逻辑语句][start,end]`
	- 缺失值及异常值处理：
		- 缺失值：
		- ![[Pasted image 20230119151430.png]]
		- ==注：dropna和fillna均可传入第二参数inplace，当其为true时会覆盖原数据，flase则不会，默认为false；dropna又可传入第三参数axis，其为0时对行操作，为1时对列操作，默认为0==
	- 异常值：
		- 在不影响整体的情况下可以进行覆盖删除
	- 数据保存：`arr.to_excel('保存至的文件路径')`
	- 数据格式转换：
		-  查看格式：`arr.dtype`
		- 转换格式：`arr.astype('')`
	- 根据值排序：`arr.sort_values(by=['首位排序依据','次位排序依据',···],ascending=)`   ==(ascending默认为true，即升序排列，false为降序)==
6. 基本统计分析：
	- 描述性统计：`arr.describe()`   ==(其中count是行数，mean是均值，std是标准差，三个百分数是统计学中的四分位数，50%是中位数)==
	- 方差：`arr.var()`
	- 相关系数：`arr[['类1','类2']].corr()`
	- 协方差：`arr[['类1','类2']].cov()`
	- 查询唯一值：`arr[].unique()`
	- 合并重复数据：`arr[].replace(['旧类1','旧类2',···],['新类1','新类2',···],inplace=)`
	- 查询唯一值出现的次数：`arr[].value_counts()`
7. 数据透视：
	- 参数设置：`pd.pivot_table(arr,index[],values[],aggfuc[]/aggfuc{},fill_value=0,margins=True)`
	- arr为传入的dataframe
	- index为需要设置成的行索引
	- values为需要设置成的列索引
	- aggfunc为对数据进行的计算函数，设置成字典可以对不同索引进行不同计算
	- fill_value=0为对非数值的数据进行填充0处理
	- margins=True为在末尾添上总和一行
8. 层次化索引：
	- Series的层次化索引：
		- ![[Pasted image 20230120161042.png]]
		- ![[Pasted image 20230120162233.png]]
		- 层次化索引转DataFrame形式：`s.unstack()`   ==(转回为s.unstack().stack()，Series在转成DataFrame时可能会产生缺失值)==
	- DataFrame的层次化索引：
		- ![[Pasted image 20230120162824.png]]
		- ![[Pasted image 20230120163101.png]]
		- ![[Pasted image 20230120163803.png]]
		- ![[Pasted image 20230120163902.png]]
		- DataFrame也有转置的操作，跟numpy中的一样
		- DataFrame也可以用stack和unstack方法，会转换成层次化索引的Series结构
	- GroupBy：
		- 特征：只会对数值型变量进行分组计算
		- 基础形式：`group=arr.groupby(arr.[''])`   ==(括号里面填写的是分组依据)==
		- 计算：`group.mean()/sum()/···`
		- ![[Pasted image 20230120171704.png]]
		- ![[Pasted image 20230120171751.png]]
		- ![[Pasted image 20230120172041.png]]
		- 
	- 

## 1月20日

### pandas的进一步学习

1. 
