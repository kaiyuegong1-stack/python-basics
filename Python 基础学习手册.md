# Python 基础学习手册

> **适用人群：** Python 零基础/有一点编程基础，希望进入 AI 开发、AI 应用开发、Agent 开发、数据分析方向。
>
> **学习目标：**
>
> - 能独立阅读 Python 代码
> - 能写出中小型 Python 项目
> - 为后续学习 NumPy、Pandas、FastAPI、LangChain、LLM 打下基础

------

# 第一章 Python简介

## 什么是Python？

Python 是一种高级编程语言，由 Guido van Rossum 于1991年发布。

它最大的特点：

- 简单易学
- 代码可读性高
- 第三方库丰富
- AI领域事实标准语言

目前几乎所有AI框架：

- PyTorch
- TensorFlow
- LangChain
- OpenAI SDK
- FastAPI

全部都是 Python。

------

## Python能做什么？

Python几乎什么都能做：

| 方向       | 是否推荐 |
| ---------- | -------- |
| Web开发    | ⭐⭐⭐⭐     |
| AI开发     | ⭐⭐⭐⭐⭐    |
| 数据分析   | ⭐⭐⭐⭐⭐    |
| 自动化办公 | ⭐⭐⭐⭐⭐    |
| 爬虫       | ⭐⭐⭐⭐     |
| 桌面软件   | ⭐⭐⭐      |
| 游戏开发   | ⭐⭐⭐      |

------

# 第二章 第一个Python程序

```
print("Hello World")
```

运行结果：

```
Hello World
```

print()

表示：

> 向控制台输出内容。

------

多个print

```
print("Hello")
print("Python")
```

输出：

```
Hello
Python
```

------

# 第三章 变量

变量就是保存数据的盒子。

例如：

```
name = "Tom"
age = 20
```

其中：

```
变量名 = 数据
```

读取变量：

```
print(name)
print(age)
```

输出：

```
Tom
20
```

------

变量可以修改：

```
age = 20

age = 21

print(age)
```

输出：

```
21
```

------

变量命名规范：

推荐：

```
user_name
student_age
total_price
```

不推荐：

```
a
b
x1
```

除非循环变量。

------

# 第四章 数据类型

Python常见数据类型：

## int（整数）

```
age = 18
```

------

## float（小数）

```
height = 1.75
```

------

## str（字符串）

```
name = "Alice"
```

字符串必须加引号。

------

## bool（布尔）

```
True
False
```

例如：

```
is_student = True
```

------

查看类型：

```
print(type(age))
```

输出：

```
<class 'int'>
```

------

# 第五章 输入输出

输出：

```
print("Hello")
```

输入：

```
name = input("请输入姓名：")
```

例如：

```
name = input("你的名字：")

print(name)
```

------

注意：

input得到的永远都是字符串。

例如：

```
age = input("年龄：")
```

如果输入：

```
18
```

实际上：

```
"18"
```

所以：

```
age = int(age)
```

------

# 第六章 类型转换

字符串转整数：

```
int("18")
```

整数转字符串：

```
str(18)
```

小数：

```
float("3.14")
```

布尔：

```
bool(1)
```

------

# 第七章 运算符

加减乘除：

```
a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

输出：

```
7
3
10
2.5
```

------

整除：

```
5 // 2
```

结果：

```
2
```

------

取余：

```
5 % 2
```

结果：

```
1
```

------

幂运算：

```
2 ** 3
```

结果：

```
8
```

------

# 第八章 字符串

拼接：

```
name = "Tom"

print("Hello " + name)
```

------

重复：

```
print("=" * 30)
```

输出：

```
==============================
```

------

长度：

```
len(name)
```

------

索引：

```
name = "Python"

print(name[0])
```

输出：

```
P
```

------

切片：

```
name[0:3]
```

结果：

```
Pyt
```

------

# 第九章 条件判断

```
age = 18

if age >= 18:
    print("成年")
```

注意：

Python依靠缩进表示代码块。

------

if else：

```
if score >= 60:
    print("及格")
else:
    print("不及格")
```

------

多个条件：

```
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

------

# 第十章 循环

for循环：

```
for i in range(5):
    print(i)
```

输出：

```
0
1
2
3
4
```

------

while循环：

```
count = 0

while count < 5:
    print(count)
    count += 1
```

------

break：

结束循环。

continue：

跳过本次循环。

------

# 第十一章 列表(List)

创建：

```
fruits = ["苹果", "香蕉", "橘子"]
```

访问：

```
print(fruits[0])
```

添加：

```
fruits.append("葡萄")
```

删除：

```
fruits.remove("香蕉")
```

遍历：

```
for fruit in fruits:
    print(fruit)
```

------

# 第十二章 元组(Tuple)

```
point = (10,20)
```

特点：

不可修改。

------

# 第十三章 字典(Dictionary)

创建：

```
user = {
    "name":"Tom",
    "age":20
}
```

读取：

```
print(user["name"])
```

新增：

```
user["city"] = "北京"
```

遍历：

```
for key,value in user.items():
    print(key,value)
```

------

# 第十四章 集合(Set)

创建：

```
nums = {1,2,3}
```

特点：

- 自动去重
- 无序

例如：

```
{1,1,2,2}
```

结果：

```
{1,2}
```

------

# 第十五章 函数(Function)

定义：

```
def hello():
    print("Hello")
```

调用：

```
hello()
```

------

带参数：

```
def add(a,b):
    return a+b
```

调用：

```
result = add(3,5)
```

------

# 第十六章 模块(Module)

导入：

```
import math
```

平方根：

```
math.sqrt(16)
```

------

导入指定函数：

```
from math import sqrt
```

------

# 第十七章 文件操作

写文件：

```
with open("test.txt","w",encoding="utf-8") as f:
    f.write("Hello")
```

读文件：

```
with open("test.txt","r",encoding="utf-8") as f:
    print(f.read())
```

------

# 第十八章 异常处理

```
try:
    num = 10/0
except:
    print("发生异常")
```

推荐：

```
try:
    ...
except ZeroDivisionError:
    ...
```

------

# 第十九章 面向对象（OOP）

定义类：

```
class Student:

    def __init__(self,name):
        self.name = name

    def study(self):
        print(self.name,"正在学习")
```

创建对象：

```
s = Student("Tom")
s.study()
```

------

# 第二十章 常用标准库

| 模块        | 用途             |
| ----------- | ---------------- |
| math        | 数学计算         |
| random      | 随机数           |
| datetime    | 日期时间         |
| os          | 操作系统         |
| pathlib     | 路径管理（推荐） |
| json        | JSON处理         |
| collections | 高级数据结构     |
| itertools   | 高效迭代         |
| re          | 正则表达式       |

------

# 第二十一章 Python 编码规范（PEP 8）

良好的代码风格有助于团队协作和代码维护：

- 使用 **4 个空格**进行缩进，不要混用 Tab。
- 变量、函数名使用 `snake_case`（如 `user_name`）。
- 类名使用 `PascalCase`（如 `StudentInfo`）。
- 常量使用全大写（如 `MAX_SIZE`）。
- 每行代码尽量不超过 **79~88** 个字符（不同工具配置略有差异）。
- 为函数和复杂逻辑添加适当注释或文档字符串（Docstring）。

示例：

```
def calculate_total(price, quantity):
    """计算商品总价"""
    return price * quantity
```

------

# 第二十二章 常见错误与调试

## SyntaxError（语法错误）

```
if True
    print("Hello")
```

原因：缺少冒号 `:`。

------

## IndentationError（缩进错误）

```
if True:
print("Hello")
```

原因：缩进不正确。

------

## NameError（变量未定义）

```
print(username)
```

确保变量已定义：

```
username = "Tom"
print(username)
```

------

## TypeError（类型错误）

```
"18" + 2
```

需要先进行类型转换：

```
int("18") + 2
```

------

# 第二十三章 AI 开发常用 Python 技巧

这些技巧在后续学习 AI、数据分析和自动化时会频繁使用：

## 列表推导式

```
squares = [x * x for x in range(5)]
print(squares)
# [0, 1, 4, 9, 16]
```

------

## 枚举遍历

```
fruits = ["苹果", "香蕉", "橘子"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

------

## 解包

```
point = (10, 20)
x, y = point
```

------

## f-string（推荐）

```
name = "Tom"
age = 20

print(f"我的名字是{name}，今年{age}岁。")
```

相比字符串拼接，可读性更高。

------

# Python 学习路线总结

建议按照以下顺序学习：

| 阶段          | 学习内容                                    | 掌握程度 |
| ------------- | ------------------------------------------- | -------- |
| ① 基础语法    | 变量、数据类型、输入输出、运算符            | ⭐⭐⭐⭐⭐    |
| ② 流程控制    | if、for、while                              | ⭐⭐⭐⭐⭐    |
| ③ 数据结构    | 列表、元组、字典、集合                      | ⭐⭐⭐⭐⭐    |
| ④ 函数与模块  | 函数、标准库、自定义模块                    | ⭐⭐⭐⭐⭐    |
| ⑤ 文件与异常  | 文件操作、异常处理                          | ⭐⭐⭐⭐     |
| ⑥ 面向对象    | 类、对象、继承、多态                        | ⭐⭐⭐⭐     |
| ⑦ Python 高级 | 列表推导式、生成器、装饰器（后续学习）      | ⭐⭐⭐      |
| ⑧ AI 常用库   | NumPy、Pandas、Matplotlib、FastAPI、PyTorch | ⭐⭐⭐⭐⭐    |

------

