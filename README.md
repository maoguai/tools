# tools

# py_updata
利用 python 向 PostgreSQL 数据库 插入数据

# read_csv
利用 python 读取 csv 表格

# fix_symboltable
在ida修复二进制文件函数表

# sort_loop_depth
在ida中搜索循环深度

# binary_conversion
进制转换

# ida_bin
IDA逆向常用宏定义

# sctest
shell code test
1） 读shellcode 二进制读到内存
2）将装载shellcode内存的属性变成可执行
3）跳到该shellcode执行
使用方法：
$ gcc -Wall -g -o sctest32 sctest.c -m32
$ gcc -Wall -g -o sctest sctest.c
$ ./sctest32 ../shell

# bind
绑定端口shellcode
使用方法：
1）nasm -o bind bind.s 2）./sctest32 bind 3)打开一个新端终，通过网络与Shellcode打开的端口进行连接，然后获取Shellcode，通过cat /etc/passwd命令获取系统帐号信息：$ netcat localhost 43690
cat /etc/passwd       

# pattern
shellcode中利用查找内存错误地址
