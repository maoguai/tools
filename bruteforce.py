#!/usr/bin/env python 
# -*- coding: utf8 -*- 

password = "000A0"

passwdSource =  ['0', '1', '2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','k',
                 'l','m','n','o','p','q','r','s','t','u','v',
                 'w','x','y','z','A','B','C','D','E','F','G',
                 'H','I','J','K','L','M','N','O','P','Q','R',
                 'S','T','U','V','W','X','Y','Z']

# 递归寻找密码
def findPwd(deep,parent) :
    # 递归直到最后一层
    if deep == 1 :
        # 判断是否与密码相同，相同返回1，否则返回0
        if (parent == password):
            print ("I had find the password: ")
            print(parent)
            return 1
        else:
            return 0
    else:
        for j in passwdSource :
            # 递归并判断子树返回值，如若返回1，则函数结束，如返回0，继续往下寻找*/
            if findPwd(deep - 1, parent + j) :
            	return 1
    return 0



def bruteforce(): 
    passwdlen = 1 
    flag = 1 
    pwd = ''
    while flag :
    	for j in passwdSource :
            if findPwd(passwdlen, pwd + j) :
            	flag = 0
            	break
        passwdlen += 1
 
if __name__ == '__main__': 
    bruteforce() 
     

