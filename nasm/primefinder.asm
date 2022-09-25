section         .data
        numout  times 18 db 0
        primes: resb 1000000
        msg:    db "Prime count: %d"

section .text
global main
extern printf

; Registers:
;       rax - None
;       rcx - 0xff
;       rdx - None
;       rdi - None
;       rsi - None
;       r8 - Number at back of seive
;       r9 - Max number in seive
;       r10 - Location of current point in seive
;       r11 - Count of primes


main:
        ;Initilise teh registers
        mov r11, 0
        mov r8, 2
        mov r9, 1000000
        mov cl, 0xff

        mov r10, 2

        ;Run the program
        call find_primes

        push r11
        push msg
        call printf
        ret

seive:
        mov r10, r8
.while:; r10 < r9
        add r10, r8

        cmp r10, r9
        jge .endwhile

        mov cl, 0xff
        mov [r10+primes], cl
        jmp .while
.endwhile:
        ret

find_primes:
.while: ;r8 < r9
        cmp r8, r9
        jnl .endwhile

        mov al, [primes+r8]
        inc r8
        cmp al, 0xff
        je .while

        inc r11
        dec r8
        call seive
        inc r8
        jmp .while
.endwhile:
        ret
