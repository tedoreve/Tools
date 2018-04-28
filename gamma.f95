program main(a,b,u,sigma)

    integer i
    real*4 y, s, x

    s = 0.0
    x = 1.1
	
	do i = 1,100
		call f(i+x,y,u,sigma)
		s = s + y
    enddo
	
    print *,s

end

subroutine f(x,y,u,sigma)

	real*4 x,y,u,sigma
	y = exp(-(x-u)**2/(2*sigma**2))

end
