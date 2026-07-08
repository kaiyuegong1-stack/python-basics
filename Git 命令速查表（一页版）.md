# Git 命令速查表（一页版）

> **适用对象：Python / AI 工程师 / 日常开发**
>
> **核心原则：先 git status，再进行下一步操作。**

------

# 一、日常开发（最常用 ⭐⭐⭐⭐⭐）

### 查看当前状态

```
git status
```

查看：

- 当前分支
- 修改了哪些文件
- 是否需要 Commit
- 是否需要 Push
- 是否有冲突

------

### 添加所有修改

```
git add .
```

添加指定文件：

```
git add 文件名
```

------

### 提交代码

```
git commit -m "Day2: add Python function examples"
```

推荐格式：

```
Day1: initialize project
Day2: add list examples
Day3: implement file operations
feat: add login module
fix: resolve file read bug
docs: update README
```

------

### 上传到 GitHub

```
git push
```

第一次：

```
git push origin main
```

------

### 获取最新代码（推荐）

```
git pull --rebase
```

避免产生多余 Merge Commit。

------

# 二、查看信息

### 查看提交历史

```
git log
```

简洁模式：

```
git log --oneline
```

图形模式（推荐）：

```
git log --oneline --graph --decorate --all
```

------

### 查看文件修改

未暂存：

```
git diff
```

已暂存：

```
git diff --cached
```

------

### 查看远程仓库

```
git remote -v
```

示例：

```
origin  https://github.com/用户名/python-basics.git
```

------

# 三、分支管理

查看本地分支：

```
git branch
```

查看所有分支：

```
git branch -a
```

创建新分支：

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

切回主分支：

```
git switch main
```

------

# 四、同步远程仓库

下载远程更新（不合并）：

```
git fetch
```

下载并合并：

```
git pull
```

推荐：

```
git pull --rebase
```

上传：

```
git push
```

------

# 五、遇到冲突

查看状态：

```
git status
```

解决冲突后：

```
git add .
git rebase --continue
```

最后：

```
git push
```

------

# 六、修改最近一次 Commit

修改提交说明：

```
git commit --amend -m "新的提交说明"
```

------

# 七、撤销操作（谨慎）

取消暂存：

```
git restore --staged 文件名
```

恢复工作区文件（丢弃未提交修改）：

```
git restore 文件名
```

> ⚠️ 会丢失未保存的修改，请确认后再使用。

------

# 八、常见状态说明

### 工作区

```
modified
```

文件修改了，但还没 add。

↓

```
git add .
```

------

### 暂存区

```
Changes to be committed
```

已经 add。

↓

```
git commit
```

------

### Ahead

```
ahead 2
```

本地多两个 Commit。

↓

```
git push
```

------

### Behind

```
behind 1
```

远程多一个 Commit。

↓

```
git pull --rebase
```

------

### Ahead + Behind

```
ahead 2, behind 1
```

双方都有更新。

↓

```
git pull --rebase
git push
```

------

# 九、开发流程（牢记）

```
修改代码
    │
    ▼
git status
    │
    ▼
git add .
    │
    ▼
git commit -m "说明"
    │
    ▼
git push
```

多人协作：

```
开始开发
    │
    ▼
git pull --rebase
    │
    ▼
修改代码
    │
    ▼
git add .
    │
    ▼
git commit
    │
    ▼
git push
```

------

# 十、错误排查

## Push 失败

```
git pull --rebase
git push
```

------

## 不知道发生了什么

```
git status
```

------

## 查看历史

```
git log --oneline --graph --decorate --all
```

------

## 查看修改

```
git diff
```

------

# 十一、推荐掌握的 12 个命令

```
git status
git add .
git commit -m ""
git push
git pull --rebase
git fetch
git diff
git log --oneline --graph --decorate --all
git branch
git switch
git remote -v
git restore
```

------

# 十二、四句口诀

✅ **先 status，再操作。**

✅ **先 Commit，再 Push。**

✅ **Push 前先 Pull（多人协作建议使用 git pull --rebase）。**

✅ **不要轻易使用 git push --force 或 git reset --hard。**