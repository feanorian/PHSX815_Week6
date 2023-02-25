
import sys
import numpy as np
from scipy.special import p_roots
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
from scipy.integrate import trapz

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
	    start = int(sys.argv[p+1])
	if '-end' in sys.argv:
	    p = sys.argv.index('-end')
	    end = int(sys.argv[p+1])
	if '-step' in sys.argv:
	    p = sys.argv.index('-step')
	    steps = int(sys.argv[p+1])
	if '-root' in sys.argv:
	    p = sys.argv.index('-root')
	    root = int(sys.argv[p+1])

	# Trapezoidal Integral  
	
	# defines the domain of the integral and the number of steps
	interval = np.linspace(start, end, steps+1)
	
	# Calculates the step size
	step_size = (end - start)/(len(interval) - 1)
	
	# Stores the value of the trapezoidal integral
	integral = 0
	
	# Calculates the trapezoidal integral
	for i in range(len(interval)-1):
	    integral += f(interval[i])
	avg = (f(interval[0]) + f(interval[-1]))/2
	trap_int = step_size *(integral + avg)

	# Gaussian-Legendre Integral
	x,w = p_roots(root)
	sums = [w[i]*f(((end - start)/2)*x[i] + (start+end)/2) for i in range(len(x))]
	gauss_int = ((end - start)/2)*np.sum(sums)

	print(f'Trapezoidal approx:  {round(trap_int,5)}')
	print(f'Gaussian-Legendre approx:   {round(gauss_int,5)}')
	print(f'Difference: {100*round(np.abs(trap_int - gauss_int)/np.abs(gauss_int),2)} %')  
	
	# Plots the function and the trapezoidal approximation
	fig, ax = plt.subplots(1,1)
	x = np.arange(start,end+1,.1)
	y = f(x)
	ax.plot(x,y, 'k-', label='f(x) actual')
	plt.text(np.min(interval),f(np.max(interval))/2 , f'Trapezoidal approx:  {round(trap_int,5)}' + '\n' + f'Gaussian-Legendre approx:   {round(gauss_int,5)}' + '\n' + f'Difference: {100*round(np.abs(trap_int - gauss_int)/np.abs(gauss_int),2)} %')
	area = trapz(f(interval), interval)
	plt.vlines(start, ymin=0, ymax=f(start), label=f'lower: {start}', colors='red')
	plt.vlines(end, ymin=0, ymax=f(end), label=f'upper: {end}', colors='green')
	ax.fill_between(interval, 0, f(interval))
	plt.ylim(f(min(interval))-5, f(max(interval))+5)
	plt.legend()
	plt.show()


