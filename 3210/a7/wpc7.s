! Fergus Kelley
! CSC 3210
! Weekly Programming Challenge 7
! Due November 3rd, 2015

! Finds the zero of y = 3x^4 − 17x^3 +14x^2 − 23^x +15
! Input: none

! Output:
! x = 10, y = 14185
! x = 9, y = 8232
! x = 8, y = 4311
! x = 7, y = 1912
! x = 6, y = 597
! x = 5, y = 0

	.section ".data"

printxy:	.asciz "x = %d, y = %d\n"


	.section ".text"

!!!!! BEGIN MAIN !!!!!
.global main
main:	save %sp, -96, %sp

	! using %l0 as our x var, set it to 10
	mov 10, %l0

	! using %l1 as our y var

loop:

	! if x < 0, goto done
	cmp %l0, %g0
	bl done
	nop

	! calculate y using the calc_y subroutine
	mov %l0, %o0
	call calc_y
	nop

	! get the returned value of y and put it in %l1
	mov %o0, %l1

	! print the value of x and y
	set printxy, %o0
	mov %l0, %o1
	mov %l1, %o2
	call printf
	nop

	! if y == 0, exit
	cmp %l1, %g0
	be done
	nop

	! x--
	sub %l0, 1, %l0

	! begin the loop again
	ba loop
	nop

done:
	ret
	restore


!!!!! BEGIN CALC_Y !!!!!
.global calc_y
calc_y:	save %sp, -96, %sp

	! Working from right to left through the terms
	! storing the working value in %l0

	! 15
	mov 15, %l0

	! -23x
	mov %i0, %o0
	mov -23, %o1
	call .mul
	nop

	! Adding the terms
	add %o0, %l0, %l0

	! x^2
	mov %i0, %o0
	mov 2, %o1
	call exp
	nop

	! 14(x^2)
	mov 14, %o1
	call .mul
	nop

	! Adding the terms
	add %o0, %l0, %l0

	! x^3
	mov %i0, %o0
	mov 3, %o1
	call exp
	nop

	! -17(x^3)
	mov -17, %o1
	call .mul
	nop

	! Adding the terms
	add %o0, %l0, %l0

	! x^4
	mov %i0, %o0
	mov 4, %o1
	call exp
	nop

	! 3(x^4)
	mov 3, %o1
	call .mul
	nop

	! Adding the terms
	add %o0, %l0, %l0

	! finally return y value
	mov %l0, %i0
	ret
	restore


!!!!! BEGIN EXP !!!!!
.global exp
exp:	save %sp, -96, %sp
	! returns %i0 to the power of %i1

	! %l0 is the loop counter
	mov %i1, %l0
	sub %l0, 1, %l0

	! %o0 will hold the solution
	mov %i0, %o0

exploop:
	cmp %l0, %g0
	ble expdone
	nop

	mov %i0, %o1
	call .mul
	nop

	sub %l0, 1, %l0

	ba exploop
	nop

expdone:
	! return exp value
	mov %o0, %i0
	ret
	restore
