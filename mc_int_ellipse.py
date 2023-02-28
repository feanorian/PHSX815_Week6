
"""
Name: Craig Brooks
PHSX 815 Spring 2023
HW # 7
Due Date 2/27/2023
This code performs Monte Carlo integration of an ellipse function, calculates the error, and plots the parameterization and 'hit/miss' regions.
The assumption is the ellipse is centered at the origin. It will still calculate the integral properly, but still has issues with the plot when not centered. This will be fixed in a future fix.

Additionally, for checking if the points were inside the ellipse, I borrowed from Stack0verflow

Source: https://stackoverflow.com/questions/37031356/check-if-points-are-inside-ellipse-faster-than-contains-point-method
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sympy 

if __name__ == "__main__":
	# if the user includes the flag -h or --help print the options
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s [-xlow -xhigh -ylow -yhigh -samp ]" % sys.argv[0])
		print
		sys.exit(1)
	if '-xlow' in sys.argv:
		p = sys.argv.index('-xlow')
		xlow = int(sys.argv[p+1])
	else:
		xlow = -3
	if '-xhigh' in sys.argv:
		p = sys.argv.index('-xhigh')
		xhigh = int(sys.argv[p+1])
	else:
		xhigh = 3
	if '-ylow' in sys.argv:
		p = sys.argv.index('-ylow')
		ylow = int(sys.argv[p+1])

	else:
		ylow = -1
	if '-yhigh' in sys.argv:
		p = sys.argv.index('-yhigh')
		yhigh = int(sys.argv[p+1])

	else:
		yhigh = 1
	if '-samp' in sys.argv:
		p = sys.argv.index('-samp')
		samples = int(sys.argv[p+1])
	else:
		samples = 10
	
	#Function to integrate
	def s(x, y):
		return 3*x**2 + 2*y**2
	
	# These functions just allow us to plot the proposal functions above and beneath our target function
	def	h(x):
		return np.full(x.shape, ylow)
	def g(x):
		return np.full(x.shape, yhigh)

	x_space = np.arange(xlow,xhigh,0.1)
	
	#allows us to paramterize an ellipse to show how well our monte carlo integration fits
	t = np.arange(0, 2*np.pi, .1)
	x = xhigh*np.cos(t)
	y = yhigh*np.sin(t)
	
	# Generates random points to be plotted
	xs = np.random.uniform(xlow, xhigh, samples)
	ys = np.random.uniform(ylow, yhigh, samples)
	# function call that plots points
	f = s(xs, ys)
	
	# Takes the average of our dunction, and multiplies by the area of the rectangle that encloses the ellipse, therefore approximating the integral
	f_avg = np.mean(f)
	f_stdev = np.std(f)
	area = (xhigh - xlow)*(yhigh - ylow)
	integral = f_avg * area
	
	# computes the error
	error = f_stdev / np.sqrt(samples)
	
	# Analytical solution
	x_a = sympy.Symbol('x')
	y_a = sympy.Symbol('y')
	actual_int = float(sympy.integrate(3*x_a**2 + 2*y_a**2, (x_a,xlow,xhigh), (y_a, ylow, yhigh)))

	print(integral)
	print(actual_int)
	print(error)

	# Plots the parameterized ellipse and the Monte Carlo approximation of the ellipse
	fig, ax = plt.subplots(1)
	#ax.set_aspect('equal')
	ell_center = (0, 0)
	ell_width = xhigh-xlow
	ell_height = yhigh-ylow
	xc = xs - ell_center[0]
	yc = ys - ell_center[1]
	cos_angle = np.cos(np.radians(180))
	sin_angle = np.sin(np.radians(180))

	xct = xc * cos_angle - yc * sin_angle
	yct = xc * sin_angle + yc * cos_angle 
	rad_cc = (xct**2/(ell_width/2.)**2) + (yct**2/(ell_height/2.)**2)

	# Set the colors. Black if outside the ellipse,red if inside
	colors_array = np.array(['black'] * len(rad_cc))
	colors_array[np.where(rad_cc <= 1.)[0]] = 'red'

	# Plots the data generate in the Monte Carlo integration
	ax.scatter(xs,ys,c=colors_array,linewidths=0.3)
	plt.plot(x, y,color='green')
	plt.plot(x_space, g(x_space), color='y')
	plt.plot(x_space, h(x_space), color='y')
	plt.vlines(xlow, ymin=ylow,ymax=yhigh,colors='y')
	plt.vlines(xhigh, ymin=ylow,ymax=yhigh, colors='y')
	plt.text(.5, 1, f'Area: {round(integral, 4)}' + '\n' 
		+f'Actual: {round(actual_int,4)}' + '\n'
		+ f'Difference (Actual vs MC) : {100*round(np.abs(actual_int - integral)/np.abs(actual_int),3)} %' + '\n'
		+ f'Error: {round(error, 4)}', color='black')
		
	plt.xlabel('x')
	plt.ylabel('y')
	plt.tight_layout()
	plt.show()
	
