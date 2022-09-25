SECTION .data
buffer: resb 65536

SECTION .text
        global main

incr:
        mov cl [buffer + r11w]
        inc cl
        mov [buffer + r11w], cl
        ret

decr:
        mov cl [buffer + r11w]
        dec cl
        mov [buffer + r11w], cl
        ret

ptrinc:
        inc r11w
        ret

ptrdec:
        dec r11w
        ret

ioin:
        mov eax, 0x3
        mov ebx, 0x1
        mov cl, [buffer + r11w]
        mov edx, 0x1
        int 80h
        mov [buffer + r11w], cl
        ret

ioout:
        mov eax, 0x4
        mov ebx, 0x1
        mov cl, [buffer + r11w]
        mov edx, 0x1
        int 80h
        ret

main:
        mov r11w, 0
        call program
        mov eax, 0x1
	xor ebx, ebx
	int 0x80

program:
.Loop0:
.Loop1:
	call ptrinc
	call ioin
.Loop2:
	call ptrdec
	cmp r11w, 0
	je .Loop2
.EndLoop2:
	cmp r11w, 0
	je .Loop1
.EndLoop1:
	ret
