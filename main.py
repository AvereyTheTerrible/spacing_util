from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

model = LpProblem(name="small-problem", sense=LpMaximize)

a = LpVariable(name="0.015625", lowBound=0, cat="Integer")
b = LpVariable(name="0.03125", lowBound=0, cat="Integer")
c = LpVariable(name="0.04", lowBound=0, cat="Integer")
d = LpVariable(name="0.125", lowBound=0, cat="Integer")
e = LpVariable(name="0.25", lowBound=0, cat="Integer")
f = LpVariable(name="0.375", lowBound=0, cat="Integer")
g = LpVariable(name="0.5", lowBound=0, cat="Integer")
h = LpVariable(name="0.875", lowBound=0, cat="Integer")

a_term = 0.015625 * a
b_term = 0.03125 * b
c_term = 0.04 * c
d_term = 0.125 * d
e_term = 0.25 * e
f_term = 0.375 * f
g_term = 0.5 * g
h_term = 0.875 * h

target = 0.53
model += (
    a_term + b_term + c_term + d_term + e_term + f_term + g_term + h_term <= target,
    "constraint",
)

model += a_term + b_term + c_term + d_term + e_term + f_term + g_term + h_term

model.solve()

for var in model.variables():
    print(f"{var.name}: {var.value()}")
