#!/usr/local/bin/python3
"""Initial implementation of complex number."""

class Cplx:

	def cinit(c, real, imag):
		c.real = real
		c.imag = imag

	def cadd(c1, c2):
		c = Cplx()
		c.real = c1.real+c2.real
		c.imag = c1.imag+c2.imag
		return c

	def cstr(c):
		return "%s+%sk" % (c.real, c.imag)

if __name__ == "__main__":
	zero = Cplx()
	Cplx.cinit(zero, 0.0, 0.0)
	one = Cplx()
	Cplx.cinit(one, 1.0, 0.0)
	i = Cplx()
	Cplx.cinit(i, 0.0, 1.0)
	result = Cplx.cadd(zero, Cplx.cadd(one, i))
	print(Cplx.cstr(result))
