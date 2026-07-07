# Learning Log

## Day 1（2026-07-07）

### 今日目标

- 搭建 Python 开发环境
- 熟悉 VS Code
- 学习 Git 和 GitHub 的基本使用
- 完成第一个 Python 程序
- 创建 Python 学习仓库

---

## 今日完成

### 1. 环境搭建

完成了以下工具的安装与配置：

- Python
- VS Code
- Git
- GitHub

成功在 VS Code 中运行了第一个 Python 程序。

---

### 2. 第一个 Python 程序

创建项目：

hello_python

编写了第一个程序：

- 输出 Hello AI World!
- 获取用户输入
- 使用 f-string 输出结果

学习内容：

- print()
- input()
- 变量
- f-string

---

### 3. GitHub 仓库规划

了解到 GitHub 不应该把所有代码放在一个仓库。

目前规划：

- ai-learning-roadmap（学习导航）
- python-basics（Python 基础）
- 后续逐步创建更多独立项目仓库

开始理解：

> 一个知识模块对应一个仓库，一个练习对应一个文件夹。

---

### 4. Git 基础

学习了：

- git init
- git status
- git add .
- git commit
- git log
- git remote

理解了：

Git 是本地版本管理工具；

GitHub 是远程代码托管平台。

代码需要先提交到本地 Git，再上传到 GitHub。

---

## 今日遇到的问题

### 1. 不知道项目应该创建在哪里

开始以为 README、main.py 等文件需要直接在 GitHub 网站创建。

后来了解到：

所有开发工作都应该在 Windows 本地完成，再通过 Git 推送到 GitHub。

---

### 2. Git 显示 nothing to commit

执行：

git status

提示：

nothing to commit, working tree clean

一开始以为提交失败。

后来了解到：

说明代码已经成功提交到本地 Git，只是没有新的修改。

---

### 3. git push 失败

执行：

git push -u origin main

提示：

Failed to connect to github.com

后来排查发现：

问题与代理（v2rayN）配置有关，而不是 Git 命令错误。

了解到：

浏览器可以访问 GitHub，并不代表 Git 一定能够正常使用代理。

后续准备继续解决代理配置问题。

---

## 今日收获

今天最大的收获不是写了一个 Python 程序，而是理解了整个开发流程：

Windows 本地开发

↓

Git 管理版本

↓

GitHub 保存和展示项目

开始建立起工程化开发的基本思维。

---

## 明日计划

- 学习变量
- 学习数据类型
- 完成更多 Python 基础练习
- 解决 Git Push 网络问题