from idaapi import *
import time

#固件加载地址
loadaddress = 0x80f0
#符号表起始位置
eaStart = + loadaddress
#符号表结束位置
eaEnd =  + loadaddress

ea = eaStart
eaEnd = eaEnd

while ea < eaEnd：
  #循环遍历修复函数名
  offset = 0 
  MakeStr(Dword(ea - offset), BADADDR)
  sName = GetString(Dword(ea - offset), -1, ASCSTR_C)
  print(sName)
  if sName:
    eaFunc = Dword(ea - offset + 4)
    MakeName(eaFunc, sName)
    MakeCode(eaFunc)
    MakeFunction(eaFunc, BADADDR)
  ea = ea + 16
  
