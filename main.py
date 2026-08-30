from polinomials.polinomials import Polinomial
from sympy import Expr


def main():
    print("Hello from polinomial-generator!")
    poli = Polinomial()
    expressions = []
    for i in range(0, 3):
        # loop for a long, 4 variable terms + 4 independent terms exercise
        expr = poli.polinomy()
        expressions.append(expr)

    print(expressions)
    # later on, each expression will be written, as if I add them now
    # they will be REALLY added instead of serially stored.


if __name__ == "__main__":
    main()
