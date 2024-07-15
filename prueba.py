
from pyswip import Prolog

prolog = Prolog()

# Assert a fact
prolog.assertz("father(michael, john)")

# Query the fact
for solution in prolog.query("father(michael, X)"):
    print(solution["X"])
