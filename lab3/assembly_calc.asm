; Muhammad Mujtaba
; CS-117; 540040
; 2k25 BESE-16B

; TESTED in ONECOMPILER ONLINE ASSEMBLER

section .data
  addMsg     db 'Addition: ',0
  addMsgLen  equ $-addMsg
  addResult  db 0,0                      ; up to 2 digits

  newline    db 10

  mulMsg     db 'Multiplication: ',0
  mulMsgLen  equ $-mulMsg
  mulResult  db 0,0                      ; up to 2 digits

section .text
  global _start

_start:
  ; ADDITION
  mov ah, 4                   ; move first number to ah ----------- INPUT A
  mov al, 4                   ; move second number to al ---------- INPUT B
  
  add al, ah                  ; add al and ah, result in al
  call to_ascii               ; stores the output in registers dl (tens) and dh (ones)
  mov [addResult], dl         ; tens (if nonzero)
  mov [addResult+1], dh       ; ones

  ; MULTIPLICATION
  mov al, 4                   ; move first number to al ----------- INPUT A
  mov bl, 4                   ; move second number to bl ---------- INPUT B

  mul bl                      ; multiply al by bl, result in ax
  call to_ascii               ; stores the output in registers dl (tens) and dh (ones)
  mov [mulResult], dl         ; tens (if nonzero)
  mov [mulResult+1], dh       ; ones

  ; PRINT "Addition: "
  mov eax,4                   ; syscall number for sys_write
  mov ebx,1                   ; file descriptor 1 is stdout
  mov ecx,addMsg              ; pointer to message to write
  mov edx,addMsgLen           ; message length
  int 0x80                    ; call kernel

  ; PRINT ADDITION RESULT
  mov eax,4                   ; syscall number for sys_write
  mov ebx,1                   ; file descriptor 1 is stdout
  mov ecx,addResult           ; pointer to result to write
  mov edx,2                   ; length is 2 (tens and ones)
  int 0x80                    ; call kernel

  ; PRINT NEWLINE
  mov eax,4                   ; syscall number for sys_write
  mov ebx,1                   ; file descriptor 1 is stdout
  mov ecx,newline             ; pointer to newline
  mov edx,1                   ; length is 1
  int 0x80                    ; call kernel

  ; PRINT "Multiplication: "
  mov eax,4                   ; syscall number for sys_write
  mov ebx,1                   ; file descriptor 1 is stdout
  mov ecx,mulMsg              ; pointer to message to write
  mov edx,mulMsgLen           ; message length
  int 0x80                    ; call kernel

  ; PRINT MULTIPLICATION RESULT
  mov eax,4                   ; syscall number for sys_write
  mov ebx,1                   ; file descriptor 1 is stdout
  mov ecx,mulResult           ; pointer to result to write
  mov edx,2                   ; length is 2 (tens and ones)
  int 0x80                    ; call kernel

  ; EXIT
  mov eax,1                   ; syscall number for sys_exit
  mov ebx,0                   ; exit code 0
  int 0x80                    ; call kernel

; converts given number in AL to ASCII in DL (tens) and DH (ones)
to_ascii:
  xor ah, ah      ; clear AH for division
  mov bl, 10      ; divisor
  div bl          ; divide AX by 10, quotient in AL, remainder in AH
  add al, '0'     ; convert to ASCII
  add ah, '0'     ; convert to ASCII
  mov dl, al      ; tens
  mov dh, ah      ; ones
  ret
