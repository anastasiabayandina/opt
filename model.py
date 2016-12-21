from pyomo.environ import *

model = AbstractModel()

#indices of vertices
model.I = Set()
#ajacency matrix
model.A = Set(within=model.I*model.I)
model.a = Param(model.A)
#weights
model.c = Param(model.I)
#variables
model.x = Var(model.I, within=IntegerSet(0, 1))

def objective(model):
	return summation(model.c, model.x)

model.OBJ = Objective(rule=objective, sense=maximize)

def constraint(model, i, j):
	return model.x[i] + model.x[j] - model.a[i,j] <= 1

model.Constraint = Constraint(model.A, rule=constraint)