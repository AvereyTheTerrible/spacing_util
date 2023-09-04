import pulp


class Model:
    def __init__(self, spacer_sizes=[]) -> None:
        self.model = pulp.LpProblem(
            name="maximize first objective", sense=pulp.LpMaximize
        )
        self.model2 = pulp.LpProblem(
            name="minimize second objective", sense=pulp.LpMinimize
        )
        self.spacer_sizes = spacer_sizes

    def solve(self, target=0.0):
        self.target = target

        lhs = pulp.LpAffineExpression()
        variables = []
        for s in self.spacer_sizes:
            variables.append(
                (s, pulp.LpVariable(name=f"{s}", lowBound=0, cat="Integer"))
            )
        for s in variables:
            lhs += s[0] * s[1]
        self.model += (
            lhs <= target,
            "constraint",
        )

        self.model.setObjective(lhs)
        self.model.solve()

        first_constraint = pulp.value(self.model.objective)

        self.model2 += (
            lhs == first_constraint,
            "constraint",
        )
        objective = pulp.LpAffineExpression()
        for s in variables:
            objective += s[1]
        self.model2.setObjective(objective)
        self.model2.solve()

        res = []
        for var in self.model2.variables():
            res.append((var, var.value()))
        return res
