 # Polinomial Generator

 A small Python package for generating random symbolic polynomial expressions
 with [SymPy](https://www.sympy.org/). It is intended for use in tutoring
 sessions and as a hands-on project for practicing writing code deliberately,
 rather than relying on vibe coding.

 > The project is currently under development. The public API and generated
 > expressions may change as more polynomial exercise types are added.

 ## Requirements

 - Python 3.14 or newer
 - [uv](https://docs.astral.sh/uv/)

 ## Installation

 Clone the repository and install its dependencies with `uv`:

 ```bash
 git clone <repository-url>
 cd polinomial_generator
 uv sync
 ```

 To use the package from another local project, install it in editable mode:

 ```bash
 uv pip install -e /path/to/polinomial_generator
 ```

 ## Development Usage

 Run the development example from the project root:

 ```bash
 uv run python main.py
 ```

 This generates three random SymPy expressions using the current defaults.

 ## Package Usage

 Import `Polinomial` and call `polinomy()` from Python:

 ```python
 from polinomials.polinomials import Polinomial

 polynomial = Polinomial()
 expression = polynomial.polinomy()

 print(expression)
 ```

 `polinomy()` returns a SymPy `Expr`. Its current parameters are:

 ```python
 polynomial.polinomy(
     degree=1,
     num_terms=2,
     variable="x y",
     accepted_ops="+-*/",
 )
 ```

 The current implementation generates terms using the `x` symbol. The `y`
 symbol is created when multiple variable names are provided, but is not yet
 used in expression generation.

 ## Project Structure

 ```text
 polinomial_generator/
 ├── main.py                      # Development runner
 ├── polinomials/
 │   ├── __main__.py
 │   └── polinomials.py           # Polinomial class
 ├── pyproject.toml               # Project metadata and dependencies
 └── uv.lock                      # Locked dependency versions
 ```

 ## License

 No license has been selected yet.
