###1. 简单shell命令
```
date 查看日期
cal 默认显示当前月份的日历
df 查看磁盘剩余空间的容量
free 显示内存使用情况
exit 结束当前终端会话
查看cpu信息：  
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
查看gpu信息：
lspci  | grep -i vga
查看具体gpu
lspci -v -s +gpu编号，gpu编号由之前的指令获得

```