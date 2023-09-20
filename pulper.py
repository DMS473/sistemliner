# from pulp import *

import pulp as p
model = p.LpProblem('linear_programming', p.LpMaximize)

# get solver
solver = p.getSolver('PULP_CBC_CMD')

# declare decision variables
x1 = p.LpVariable('x1', lowBound = 0, cat = 'continuous')
x2 = p.LpVariable('x2', lowBound = 0, cat = 'continuous')


# # declare objective
# model += 10*x1 + 5*x2

# # declare constraints
# model += x1 + x2 <= 24
# model += 10*x1 <= 100
# model += 5*x2 <= 100


# Tes 1

# declare objective
model += 6*x1 + 10*x2

# declare constraints
model += x1 + x2 <= 12
model += x1 + 2*x2 <= 20
# model += 10*x1 <= 100
# model += 5*x2 <= 100


# solve 
results = model.solve(solver=solver)

# print results
if p.LpStatus[results] == 'Optimal': print('The solution is optimal.')
print(f'Objective value: z* = {p.value(model.objective)}')
print(f'Solution: x1* = {p.value(x1)}, x2* = {p.value(x2)}')
# The solution is optimal.
# Objective value: z* = 170.0
# Solution: x1* = 10.0, x2* = 14.0
