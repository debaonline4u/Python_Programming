from string import Template

# here t is a template which has placeholder for value of x
t=Template("x is $x")
print(t.substitute({'x':1}))

