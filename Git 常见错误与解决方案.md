# Git 常见错误与解决方案

> 适用于 Git 初学者、Python 学习者、AI 工程师求职准备。
>
> 核心原则：**先看 git status，再决定下一步。**

------

# 一、Git 常见工作流程（推荐）

每次开发建议遵循固定流程：

```
开始开发
    │
    ▼
修改代码
    │
    ▼
git status
    │
    ▼
git add .
    │
    ▼
git commit -m "本次修改说明"
    │
    ▼
git push
    │
    ▼
完成
```

如果多人协作：

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

# 二、遇到问题第一步

无论 Git 报什么错，第一步永远执行：

```
git status
```

Git 会告诉你：

- 当前在哪个分支
- 是否有未提交代码
- 是否需要 Pull
- 是否需要 Push
- 是否存在冲突

**不要盲目复制网上的命令。**

------

# 三、Push 被拒绝（最常见）

## 报错

```
! [rejected] main -> main (non-fast-forward)
error: failed to push some refs
```

## 原因

GitHub 已经有新的提交。

你的本地历史：

```
A → B → C
```

GitHub：

```
A → B → D
```

Git 不知道应该保留哪一个。

------

## 正确解决方案

```
git pull --rebase origin main
git push
```

流程图：

```
Push失败
    │
    ▼
git pull --rebase
    │
    ▼
是否冲突？
    │
 ┌───┴────┐
 │        │
否       是
 │        │
 ▼        ▼
git push 解决冲突
          │
          ▼
git add .
          │
          ▼
git rebase --continue
          │
          ▼
git push
```

------

# 四、Merge Conflict（冲突）

## 报错

```
CONFLICT (content)
```

Git 无法判断保留哪部分内容。

例如：

```
<<<<<<< HEAD
本地内容
=======
远程内容
>>>>>>> origin/main
```

------

## 解决步骤

### 第一步

打开冲突文件。

保留需要的内容。

删除：

```
<<<<<<<
=======
>>>>>>>
```

------

### 第二步

```
git add .
```

------

### 第三步

如果是 Rebase：

```
git rebase --continue
```

如果是 Merge：

```
git commit
```

------

### 第四步

```
git push
```

------

# 五、忘记 git add

现象：

```
git commit -m "..."
```

Git 提示：

```
nothing added to commit
```

原因：

没有进入暂存区。

解决：

```
git add .
git commit -m "..."
```

------

# 六、忘记 Commit 就 Push

现象：

```
git push
```

Git：

```
Everything up-to-date
```

实际上：

代码没有上传。

原因：

代码还在工作区。

流程：

```
工作区
    │
git add
    │
暂存区
    │
git commit
    │
本地仓库
    │
git push
    │
GitHub
```

少任何一步都不会上传代码。

------

# 七、误删代码

如果：

```
还没有 Commit
```

恢复难度较大。

如果：

```
已经 Commit
```

Git 基本都可以恢复。

因此建议：

**经常 Commit。**

------

# 八、Commit 信息写错

最近一次：

```
git commit --amend -m "新的提交说明"
```

例如：

```
git commit --amend -m "Day2: add function examples"
```

------

# 九、提交了不该提交的文件

例如：

```
__pycache__
.idea
.vscode
```

应该：

```
git rm --cached 文件名
```

然后：

添加：

```
.gitignore
```

例如：

```
__pycache__/
*.pyc
.vscode/
.idea/
```

------

# 十、进入 Detached HEAD

例如：

```
HEAD detached at 4638dde
```

原因：

切换到了某个 Commit。

解决：

```
git switch main
```

不要继续开发。

------

# 十一、Ahead / Behind 看不懂

## Ahead

例如：

```
ahead 2
```

表示：

本地比 GitHub 多两个 Commit。

流程：

```
本地
A
│
B
│
C
│
D
↑
ahead 2

GitHub
A
│
B
```

解决：

```
git push
```

------

## Behind

例如：

```
behind 3
```

说明：

GitHub 更新了。

流程：

```
GitHub
A
│
B
│
C
│
D

本地
A
│
B
```

解决：

```
git pull
```

------

## Ahead + Behind

例如：

```
ahead 2, behind 1
```

表示：

双方都修改了。

流程：

```
本地

A
│
B
│
C
│
D

GitHub

A
│
B
│
E
```

解决：

```
git pull --rebase
git push
```

------

# 十二、为什么推荐 Rebase

Merge：

```
A
│
B
├────C
│
D
│
Merge
```

历史比较复杂。

Rebase：

```
A
│
B
│
D
│
C'
```

提交记录更整洁。

学习阶段推荐：

```
git pull --rebase
```

------

# 十三、Fetch、Pull、Push 的区别

```
GitHub
    ▲
    │
push
    │
本地仓库
    ▲
    │
commit
    │
暂存区
    ▲
    │
add
    │
工作区
```

另外：

```
GitHub
    │
 fetch
    ▼
本地仓库（不修改工作区）
```

而：

```
GitHub
    │
 pull
    ▼
自动下载 + 自动合并
```

总结：

| 命令      | 作用         |
| --------- | ------------ |
| git fetch | 下载，不合并 |
| git pull  | 下载并合并   |
| git push  | 上传         |

------

# 十四、Reset 与 Revert

## git reset

作用：

回退历史。

例如：

```
git reset --soft HEAD~1
```

保留代码。

------

```
git reset --hard HEAD~1
```

危险。

代码会丢失。

学习阶段尽量不要使用：

```
git reset --hard
```

------

## git revert

不会删除历史。

而是：

创建一个新的 Commit。

企业开发更推荐：

```
git revert CommitID
```

------

# 十五、什么时候使用 GitLens

推荐：

✅ 查看 Commit

✅ 查看作者

✅ 查看修改历史

✅ 查看 Diff

------

不推荐：

刚学习 Git 时：

❌ Pull

❌ Push

❌ Sync

因为：

GitLens 本质上执行的是：

```
Pull
↓
Merge/Rebase
↓
Push
```

出错后不容易知道是哪一步失败。

建议熟悉 Git 原理后，再用 GitLens 完成这些操作。

------

# 十六、Git 排错决策图

```
Git 出错
    │
    ▼
git status
    │
    ▼
──────────────────────────────
│ 是否有未提交修改？          │
──────────────────────────────
        │
   是───┴────否
   │            │
git add         是否 Ahead？
git commit      │
                │
         是─────┴────否
         │             │
     git push      是否 Behind？
                     │
               是────┴────否
               │            │
      git pull --rebase   是否冲突？
                           │
                     是────┴────否
                     │            │
               修改冲突文件     完成
               git add .
               git rebase --continue
               git push
```

------

# 十七、学习阶段必须熟练掌握的命令

```
git status
git add .
git commit -m ""
git push
git pull --rebase
git fetch
git log --oneline --graph --decorate --all
git diff
git branch
git switch
git remote -v
```

熟练掌握这些命令，已经能够应对绝大多数学习、个人项目和 AI 工程开发中的 Git 场景。

------

# 十八、记住这四句话

> **第一句：先 git status，不要猜。**

> **第二句：代码没 Commit，就没有真正保存。**

> **第三句：Push 前先确认远程有没有更新。**

> **第四句：不要轻易使用 git push --force 和 git reset --hard。**