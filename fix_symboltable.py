from idaapi import *
from idc import *

loadaddress = 0x
eaStart = 0x301e64 + loadaddress
eaEnd = 0x3293a4 + loadaddress

ea = eaStart
eaEnd = eaEnd
while ea < eaEnd:
    create_strlit(Dword(ea), BADADDR)
    sName = get_strlit_contents(Dword(ea))
    print (sName)
    if sName:
        eaFunc = Dword(ea + 4)
        MakeName(eaFunc, sName)
        MakeCode(eaFunc)
        MakeFunction(eaFunc, BADADDR)
    ea = ea + 16
  ea = ea + 16
  
