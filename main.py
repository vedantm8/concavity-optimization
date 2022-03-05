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