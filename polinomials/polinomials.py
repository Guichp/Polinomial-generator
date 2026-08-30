# this file will contain the parent class for the different polinomial types the program will be will be woking with
import sympy as sp
from sympy import symbols
from random import randint
from sympy import Expr


class Polinomial:
    # These are default values for the generation of polinomials (might be unused, review)
    degree: int
    num_terms: int
    variable: str
    accepted_ops: str

    def __init__(
        self, degree=1, num_terms=2, variable="x", accepted_ops="+-*/"
    ) -> None:
        # This function builds a polinomial and returns it for later redering. Pending behaviour revision
        self.degree = degree
        self.num_terms = num_terms
        self.variable = variable
        self.accepted_ops = accepted_ops

    def polinomy(
        self, degree=1, num_terms=2, variable="x y", accepted_ops="+-*/"
    ) -> Expr:
        """
        degree=1
        num_terms=2
        variable="x y"
        accepted_ops="+-*
        """
        # first iteration of this only with one variable
        x, y = symbols(variable)
        expression = 0
        coeficient = 0
        # watch out the degree-num_terms relationship as it can cause trouble
        for i in range(0, num_terms):
            op = randint(0, 1)
            if op == 1:  # addition
                coeficient = randint(1, 30)
                expression = expression + coeficient * x ** (degree - i)
                print(i)
            else:  # substraction
                coeficient = randint(1, 30)
                expression = expression - coeficient * x ** (degree - i)
                print(i)

        print(f"Expression: {expression}")
        print(type(expression))

        return expression
