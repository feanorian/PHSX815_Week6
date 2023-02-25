
"""
Name: Craig Brooks
PHSX 815 Spring 2023
HW # 6
Due Date 2/24/2023
This code reads performs numerical integration on a function using the trapezoid method and Gaussian quadrature
"""



import sys
import numpy as np
from scipy.special import p_roots
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
from scipy.integrate import trapz
import sympy 


if __name__ == "__main__":

	def f(x):
		return x**5 - 4*x**4 + 7*x**3 + x**2 - 2*x +3 

	# if the user includes the flag -h or --help print the options
	if '-h' in sys.argv or '--help' in sys.argv:
	    print ("Usage: %s [-start -end -step ]" % sys.argv[0])
	    print
	    sys.exit(1)

	if '-start' in sys.argv:
	    p = sys.argv.index('-start')
	    start = float(sys.argv[p+1])
	if '-end' in sys.argv:
	    p = sys.argv.index('-end')
	    end = float(sys.argv[p+1])
	if '-step' in sys.argv:
	    p = sys.argv.index('-step')
	    steps = int(sys.argv[p+1])
	if '-root' in sys.argv:
	    p = sys.argv.index('-root')
	    root = int(sys.argv[p+1])

	left= 0
	bottom= .5

	# Trapezoidal Integral for n steps 
	interval = np.linspace(start, end, steps+1)
	
	step_size = (end - start)/(len(interval) - 1)
	integral = 0
	for i in range(len(interval)-1):
	    integral += f(interval[i])
	    
	avg = (f(interval[0]) + f(interval[-1]))/2
	trap_int = step_size *(integral + avg)

	# Gaussian-Legendre Integral
	x,w = p_roots(root)
	sums = [w[i]*f(((end - start)/2)*x[i] + (start+end)/2) for i in range(len(x))]
	gauss_int = ((end - start)/2)*np.sum(sums)

	# Analytical solution

	xx = sympy.Symbol('x')
	yy = sympy.Symbol('y')
	actual_int = float(sympy.integrate(xx**5 - 4*xx**4 + 7*xx**3 + xx**2 - 2*xx + 3, (xx,start,end)))

	print(f'Trapezoidal approx:  {round(trap_int,5)}')
	print(f'Gaussian-Legendre approx:   {round(gauss_int,5)}')
	print(f'Actual: {round(actual_int,5)}')
	print(f'Difference (Trap-Gauss): {100*round(np.abs(trap_int - gauss_int)/np.abs(gauss_int),2)} %')  
	print(f'Difference (Trapezoidal): {100*round(np.abs(actual_int - trap_int)/np.abs(actual_int),2)} %')
	print(f'Difference (Gaussian-Legendre): {100*round(np.abs(actual_int - gauss_int)/np.abs(actual_int),2)} %')

	# Plots the function and the trapezoidal approximation
	fig, ax = plt.subplots(1,1)
	x = np.arange(start,end+1,.1)
	y = f(x)
	ax.plot(x,y, 'k-', label='f(x) actual')
	ax.text(left,bottom, f'Trapezoidal approx:  {round(trap_int,5)}' + '\n'
		+ f'Gaussian-Legendre approx:   {round(gauss_int,5)}' + '\n' 
		+ f'Actual: {round(actual_int,5)}' + '\n'
		+ f'Difference (Trap-Gauss): {100*round(np.abs(trap_int - gauss_int)/np.abs(gauss_int),2)} %' + '\n'
		+ f'Difference (Trapezoidal): {100*round(np.abs(actual_int - trap_int)/np.abs(actual_int),2)} %' + '\n'  
		+ f'Difference (Gaussian-Legendre): {100*round(np.abs(actual_int - gauss_int)/np.abs(actual_int),2)} %')
	area = trapz(f(interval), interval)
	plt.vlines(start, ymin=0, ymax=f(start), label=f'lower: {start}', colors='red')
	plt.vlines(end, ymin=0, ymax=f(end), label=f'upper: {end}', colors='green')
	ax.fill_between(interval, 0, f(interval))
	plt.ylim(f(min(interval)), f(max(interval))+f(max(interval))*2)
	plt.legend()
	plt.show()


