from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

model = LpProblem(name="small-problem", sense=LpMaximize)

a = LpVariable(name="a", lowBound=0)
b = LpVariable(name="b", lowBound=0)
c = LpVariable(name="c", lowBound=0)
d = LpVariable(name="d", lowBound=0)
e = LpVariable(name="e", lowBound=0)
f = LpVariable(name="f", lowBound=0)
g = LpVariable(name="g", lowBound=0)
h = LpVariable(name="h", lowBound=0)


model += (0.015625 * a + 0.03125 * b + 0.04 * c + 0.125 * d + 0.25 * e + 0.375 * f + 0.5 * g + 0.875 * h <= 0.5, "constraint")
model += 0.015625 * a + 0.03125 * b + 0.04 * c + 0.125 * d + 0.25 * e + 0.375 * f + 0.5 * g + 0.875 * h

model.solve()

for var in model.variables():
	print(f"{var.name}: {var.value()}")