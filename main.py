import sympy as sym

# Creating the original equation 
x, y = sym.symbols('x y')
orig_func = 4000*x - 33*x**2 - (2*x**3 - 3*x**2 + 400*x +5000) # input your own function here
print("Original Function = ", orig_func)

# First derivative to find critical values 
dxdy = sym.diff(orig_func,x)
print("Derived Equation = ", dxdy)
critical_values = sym.solve(dxdy)
print("Critical Values = ", critical_values)

# Find the second derivative 
d2xdy2 = sym.diff(dxdy, x)
print("Second Derivative = ", d2xdy2)
# Set second derivative to 0 and find inflection points 
inflec_points = sym.solve(d2xdy2)
print("Inflection points  = ", inflec_points)
# Plug in critical values into second derivative to check for relative minima/maxima and for concavity 
relative_minima = []
relative_maxima = []
for num in critical_values:
    evaluate = d2xdy2.evalf(subs={x: num})
    if(evaluate > 0):
        relative_minima.append(num)
    elif(evaluate < 0):
        relative_maxima.append(num)

print(f"Relative Minima / Convex = {relative_minima}")
print(f"Relative Maxima / Concave = {relative_maxima}")

for num in relative_minima: 
    eval = orig_func.evalf(subs={x: num})
    print(f"x is minimized, such that x[{num}] = {eval}")

for num in relative_maxima:
    eval = orig_func.evalf(subs={x: num})
    print(f"x is maximized, such that x[{num}] = {eval}")