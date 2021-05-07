; Hello World written in x86 assembly 
;
; Created by: shyraffy
; Date 08-03-20221


global _start

section .data
	msg db "Hello, world", 0x0a ; stores "Hello world" into msg
	len equ $-msg ; stores the length of msg into len	
section .text
_start:
	mov eax, 4 ; write syscall
	mov ebx, 1 ; stoud file descriptor (first argument of write())
	mov ecx, msg ; bytes to write (second argument)
	mov edx, len ; number of bytes to write (third argument)	
	int 0x80 ; perform syscall
	
	mov eax, 1 ; exit syscall
	mov ebx, 0 ; exit code status 0
	int 0x80
