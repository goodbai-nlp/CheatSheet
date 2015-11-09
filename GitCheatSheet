git init 初始化git仓库
git add <file> 添加文件到版本库
git commit -m "注释"
git status 显示工作区状态
git diff 查看修改的内容
git reset --hard commit_id (前几位就可以) HEAD指向当前id HEAD^:前一个id
git log 查看版本库提交历史 --pretty=oneline 参数只显示id和注释
git reflog 查看命令历史
工作区->git add ->版本库->
git checkouchakanfent -- <文件>直接丢弃工作区的修改，让此文件回到最近一次git commit或git add时的状态，或者说用版本库的版本替代工作区的版本
git reset HEAD <file> 去掉暂存区的更改
git rm <file> 从git库中删除该文件
git remote add origin git@server-name:path/repo-name.git 要关联一个远程库
git push -u origin master 第一次推送master分支的所有内容
git push origin master  推送最新修改
git clone 协议+地址
git协议:git clone git@github.com:username/gitskills.git   快 ssh支持
git checkout -b local-branchname origin/remote_branchname  clone remote branch to local branch  
http协议:git clone https://github.com/michaelliao/gitskills.git
git branch 查看分支
git branch <name> 创建分支
git checkout <name> 切换到分支
git checkout -b <name> 创建并切换到分支
git merge <name> 合并某分支倒当前分支
git branch -d <name> 删除分支
git merge --no-ff -m "注释" dev 禁用fast forward 模式合并，用普通模式
git stash 当master出现bug时，可以用git stash 储存现场，修复bug后
git stash pop 返回现场（dev分支下）。
git branch -D <name> 强行删除一个未合并的分支。
git remote -v 查看版本库信息
git push origin branch-name 从本地推送分支
git tag <name> 新建一个标签，默认为head，也可以指定一个id
git tag -a <tagname> -m "标签信息" 指定标签信息
git tag 查看所有标签
git show <tagname> 查看标签信息
git push origin <tagname> 推送一个本地标签
git push origin --tags 推送所有未推送的本地标签
git tag -d <tagname>  删除一个本地标签
git push origin :refs/tags/<tagname> 删除一个远程标签
git config --global alias.st status  命令简化，alias.后的是简化后命令，后接命令当前用户的命令简化文件:用户根目录下.gitconfig文件
