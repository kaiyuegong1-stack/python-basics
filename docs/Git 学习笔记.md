# Git 学习笔记

## 一、Git 是什么？

Git 是一个**分布式版本控制工具（Version Control System）**，用于记录代码的每一次修改。

它可以帮助我们：

- 保存每一次代码修改记录
- 回退到历史版本
- 多人协作开发
- 将代码同步到 GitHub
- 管理不同开发分支

对于 AI 工程师来说，Git 是必备技能，也是面试中经常考察的内容。

------

# 二、Git 的工作流程

Git 的工作流程可以理解为四个区域：

```
工作区（Working Directory）
        │
        ▼
暂存区（Staging Area）
        │
        ▼
本地仓库（Local Repository）
        │
        ▼
GitHub（Remote Repository）
```

每个区域的作用如下：

## 1. 工作区（Working Directory）

工作区就是你正在编辑的项目文件。

例如：

```
python-basics
│
├── hello.py
├── README.md
└── notes.md
```

修改了 `hello.py` 后，Git 会检测到文件发生了变化。

查看状态：

```
git status
```

可能看到：

```
modified: hello.py
```

说明文件已经修改，但还没有提交。

------

## 2. 暂存区（Staging Area）

执行：

```
git add hello.py
```

或者：

```
git add .
```

作用：

告诉 Git：

> 我要把这些修改加入下一次提交。

注意：

此时修改只是进入暂存区，还没有生成历史版本。

查看状态：

```
git status
```

可能显示：

```
Changes to be committed:
```

------

## 3. 本地仓库（Local Repository）

执行：

```
git commit -m "Day2: add list examples"
```

作用：

创建一个新的历史版本（Commit）。

例如：

```
4638dde Day2: add list examples
```

其中：

```
4638dde
```

叫做 **Commit Hash（提交 ID）**。

每次 Commit 都是一个历史快照，可以随时回退查看。

------

## 4. 远程仓库（Remote Repository）

执行：

```
git push
```

作用：

把本地 Commit 上传到 GitHub。

上传完成后：

GitHub 和本地代码保持一致。

------

# 三、Git 常用命令

## 查看状态

```
git status
```

作用：

查看：

- 当前所在分支
- 哪些文件修改了
- 哪些文件已经暂存
- 是否需要 Push

这是最常用的命令之一。

------

## 添加文件

添加单个文件：

```
git add hello.py
```

添加所有文件：

```
git add .
```

------

## 提交

```
git commit -m "Day2: complete function examples"
```

推荐 Commit 信息：

```
Day2: add list examples
Day2: implement function demo
Day3: add file operation examples
```

不要使用：

```
update
fix
修改
test
```

这些信息无法体现项目内容。

------

## 上传

```
git push
```

第一次可以：

```
git push origin main
```

以后：

```
git push
```

即可。

------

## 下载最新代码

```
git pull
```

等价于：

```
git fetch
git merge
```

作用：

下载 GitHub 最新代码并自动合并。

------

## 仅下载，不合并

```
git fetch
```

作用：

仅获取远程更新，不影响本地代码。

适合先查看变化，再决定是否合并。

------

## 查看提交历史

完整：

```
git log
```

简洁：

```
git log --oneline
```

图形化：

```
git log --oneline --graph --decorate --all
```

例如：

```
* 4638dde Day2
* e69cecc add first script
* 689e0d8 Day1
```

------

## 查看差异

查看未暂存修改：

```
git diff
```

查看暂存后的修改：

```
git diff --cached
```

------

## 查看分支

查看本地：

```
git branch
```

查看所有：

```
git branch -a
```

创建分支：

```
git branch feature/login
```

切换分支：

```
git switch feature/login
```

创建并切换：

```
git switch -c feature/login
```

------

## 查看远程仓库

```
git remote -v
```

例如：

```
origin
https://github.com/用户名/python-basics.git
```

其中：

```
origin
```

只是远程仓库的默认名称。

------

# 四、理解 Ahead 与 Behind

例如：

```
ahead 2
```

表示：

本地比 GitHub 多两个 Commit。

需要：

```
git push
```

------

例如：

```
behind 1
```

表示：

GitHub 比本地多一个 Commit。

需要：

```
git pull
```

------

例如：

```
ahead 2, behind 1
```

表示：

双方都有新的提交。

通常使用：

```
git pull --rebase origin main
```

处理后再：

```
git push
```

------

# 五、Rebase 是什么？

假设：

本地：

```
A
│
B
│
C
```

GitHub：

```
A
│
B
│
D
```

直接 Push：

失败。

使用：

```
git pull --rebase origin main
```

Git 会把：

```
D
```

放到前面：

```
A
│
B
│
D
│
C'
```

这样提交历史更加整洁。

学习阶段建议优先使用：

```
git pull --rebase
```

------

# 六、解决冲突

如果出现：

```
CONFLICT (content)
```

步骤：

查看状态：

```
git status
```

打开冲突文件：

```
<<<<<<< HEAD
自己的内容
=======
远程内容
>>>>>>> origin/main
```

修改完成：

```
git add .
git rebase --continue
```

最后：

```
git push
```

------

# 七、推荐开发流程

每天学习建议保持固定流程：

```
git status
git add .
git commit -m "Day3: add dictionary examples"
git push
```

如果多人协作：

```
git pull --rebase
git add .
git commit -m "..."
git push
```

------

# 八、GitLens 与命令行

GitLens 是 VS Code 的 Git 可视化插件，它会调用 Git 命令完成操作。

建议：

使用 GitLens：

- 查看历史
- 查看文件修改
- 查看 Commit
- 查看作者

使用命令行：

- git add
- git commit
- git pull
- git push
- git rebase

学习 Git 的前期，命令行更容易理解每一步发生了什么，也更容易排查错误。

------

# 九、常见问题

## Push 被拒绝

原因：

远程有新的 Commit。

解决：

```
git pull --rebase origin main
git push
```

------

## 工作区很乱

查看：

```
git status
```

先确认哪些文件发生了变化，再决定是否提交。

------

## 不知道自己在哪个分支

```
git branch
```

当前分支前面会有：

```
*
```

------

# 十、AI 工程师推荐掌握的 Git 命令

```
git status
git add .
git commit -m ""
git push
git pull --rebase
git fetch
git log --oneline --graph --decorate --all
git branch
git switch
git diff
git remote -v
```

熟练掌握以上命令，已经足以满足绝大多数 AI 工程开发和求职场景。

------

# 十一、我的学习建议

对于学习 AI 和求职来说，建议养成以下习惯：

- 每完成一个知识点就提交一次 Commit。
- Commit 信息清晰描述本次学习内容。
- 每天结束前 Push 到 GitHub。
- 经常使用 `git status` 检查仓库状态。
- 遇到问题先阅读 Git 提示信息，再分析原因，不要急于使用 `git push --force`。

坚持记录完整的学习过程，比一次性上传大量代码，更能体现持续学习和工程实践能力。