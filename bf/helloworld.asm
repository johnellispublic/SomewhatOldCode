SECTION .data
buffer: times 65536 db 0
pointer: dw 0

SECTION .text
        global _start

incr:
        mov ax, bx
        mov cl, [buffer + bx]
        inc cl
        mov [buffer + bx], cl
        ret

decr:
        mov ax, bx
        mov cl, [buffer + bx]
        dec cl
        mov [buffer + bx], cl
        ret

ptrinc:
        inc ax
        ret

ptrdec:
        dec ax
        ret

ioin:
        mov ax, bx
        mov cl, [buffer + bx]
        mov ax, [pointer]
        mov eax, 0x3
        mov ebx, 0x1
        mov edx, 0x1
        int 80h
        mov [buffer + bx], cl
        mov [pointer], ax

        ret

ioout:
        mov ax, [pointer]
        mov eax, 0x4
        mov ebx, 0x1
        mov cl, [buffer + bx]
        mov edx, 0x1
        int 80h
        mov [pointer], ax
        ret

_start:
        call program
        mov ax, 0
        mov eax, 0x1
	xor ebx, ebx
	int 0x80

program:
        ret
.Loop0:
.Loop1:
	call ioin
	call ioout
.Loop2:
	call ioout
	test ax, ax
	je .Loop2
.EndLoop2:
	call ioin
	call ioout
	call ioout
	call ioin
	call ioin
	call ioin
	call incr
	call ioin
	call decr
	call ioin
	call ptrdec
	call ptrinc
	call ioin
.Loop3:
	test ax, ax
	je .Loop3
.EndLoop3:
	call ioout
	call ioout
	test ax, ax
	je .Loop1
.EndLoop1:
	call incr
	call incr
	call incr
	call incr
	call incr
	call incr
	call incr
	call incr
.Loop4:
	call ptrinc
	call incr
	call incr
	call incr
	call incr
.Loop5:
	call ptrinc
	call incr
	call incr
	call ptrinc
	call incr
	call incr
	call incr
	call ptrinc
	call incr
	call incr
	call incr
	call ptrinc
	call incr
	call ptrdec
	call ptrdec
	call ptrdec
	call ptrdec
	call decr
	test ax, ax
	je .Loop5
.EndLoop5:
	call ptrinc
	call incr
	call ptrinc
	call incr
	call ptrinc
	call decr
	call ptrinc
	call ptrinc
	call incr
.Loop6:
	call ptrdec
	test ax, ax
	je .Loop6
.EndLoop6:
	call ptrdec
	call decr
	test ax, ax
	je .Loop4
.EndLoop4:
	call ptrinc
	call ptrinc
	call ioout
	call ptrinc
	call decr
	call decr
	call decr
	call ioout
	call incr
	call incr
	call incr
	call incr
	call incr
	call incr
	call incr
	call ioout
	call ioout
	call incr
	call incr
	call incr
	call ioout
	call ptrinc
	call ptrinc
	call ioout
	call ptrdec
	call decr
	call ioout
	call ptrdec
	call ioout
	call incr
	call incr
	call incr
	call ioout
	call decr
	call decr
	call decr
	call decr
	call decr
	call decr
	call ioout
	call decr
	call decr
	call decr
	call decr
	call decr
	call decr
	call decr
	call decr
	call ioout
	call ptrinc
	call ptrinc
	call incr
	call ioout
	call ptrinc
	call incr
	call incr
	call ioout
	ret