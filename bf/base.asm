SECTION .data
buffer: times 65536 db 0
pointer: dw 0

SECTION .text
        global _start

incr:
        xor ebx, ebx
        mov ax, bx
        mov cl, [buffer + ebx]
        add cl, 1
        mov [buffer + ebx], cl
        ret

decr:
        xor ebx, ebx
        mov ax, bx
        mov cl, [buffer + ebx]
        dec cl
        mov [buffer + ebx], cl
        ret

ptrinc:
        inc ax
        ret

ptrdec:
        dec ax
        ret

ioin:
        xor ebx, ebx
        mov ax, bx
        mov cl, [buffer + ebx]
        mov ax, [pointer]
        mov eax, 0x3
        mov ebx, 0x1
        mov edx, 0x1
        int 80h
        mov [buffer + ebx], cl
        mov [pointer], ax

        ret

ioout:
        xor ebx, ebx
        mov ax, [pointer]
        mov ax, bx
        mov cl, [buffer + ebx]

        mov eax, 0x4
        mov ebx, 0x1
        mov edx, 0x1
        int 80h
        mov [pointer], ax
        ret

_start:
        mov ax, 0
        call program
        mov eax, 0x1
	xor ebx, ebx
	int 0x80

program:
        ret
