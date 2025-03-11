from orbitals import OrbitalMotion

eq = OrbitalMotion(G= 1, M = 1)
t, state = 0, [1,1,1,1]
derivatives = eq(t,state)
print(derivatives)