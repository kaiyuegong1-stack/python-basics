print("苹果", "香蕉", "橘子", sep="、")  # 输出：苹果、香蕉、橘子
print("第一行", end="----")            # 输出不换行，以----结尾
print("第二行")                        # 实际输出：第一行----第二行

name = "Alice"
score = 95.5
print(f"考生：{name}，成绩：{score:.1f}分")  # :.1f 表示保留1位小数
# 输出：考生：Alice，成绩：95.5分

age = input("请输入年龄：")   # 假设输入 18
print(type(age))            # 输出：<class 'str'>
# print(age + 1)            # 报错！字符串不能加整数