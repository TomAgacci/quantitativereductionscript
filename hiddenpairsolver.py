# ============================================================
# Universal LaVey Hidden‑Pair Solver
# Type ANY expression for x or y.
# Leave the other expression blank ("").
# Program finds the missing variable automatically.
# Variables plugged in BEFORE reduction.
# No SymPy, pure arithmetic.
# ============================================================

# ---- USER INPUT ---------------------------------------------------
# Type ONE of these. Leave the other as "".

x_expr = ""        # Example: "24/11"
y_expr = "8*x + 5" # Example: "8*x + 5"

# ---- BASIC EVAL HELPERS -------------------------------------------
def eval_fraction(expr):
    """Evaluate a/b style expressions without SymPy."""
    expr = expr.strip()
    if "/" in expr:
        a, b = expr.split("/")
        return float(a) / float(b)
    return float(expr)

def eval_expression(expr):
    """Evaluate simple arithmetic expressions using eval."""
    return eval(expr)

# ---- CORE LOGIC ---------------------------------------------------
if x_expr != "" and y_expr != "":
    raise ValueError("Type ONLY x_expr OR y_expr, not both.")

if x_expr != "":
    # User typed x, so compute x first
    x = eval_fraction(x_expr)

    # Plug x into y BEFORE reducing
    y_subbed = y_expr.replace("x", f"({x_expr})")
    y = eval_expression(y_subbed)

elif y_expr != "":
    # User typed y, so compute y first
    y = eval_fraction(y_expr)

    # Plug y into x BEFORE reducing
    x_subbed = x_expr.replace("y", f"({y_expr})")
    x = eval_expression(x_subbed)

else:
    raise ValueError("You must type an expression for x OR y.")

# ---- SLOPE ---------------------------------------------------------
slope = y / x

# ---- QUADRANT MIRROR TABLE ----------------------------------------
Q1 = ( x,  y)
Q2 = (-x,  y)
Q3 = ( x, -y)
Q4 = (-x, -y)

quadrant_table = {
    "Q1_internal_ideal": Q1,
    "Q2_internal_shadow": Q2,
    "Q3_external_ideal": Q3,
    "Q4_external_shadow": Q4
}

# ---- OUTPUT --------------------------------------------------------
print("--------------------------------------------------")
print("Universal LaVey Hidden‑Pair Solver")
print("--------------------------------------------------")
print(f"x = {x}")
print(f"y = {y}")
print(f"Slope (y/x) = {slope}")
print("--------------------------------------------------")
print("Quadrant Mirror Table:")
for name, val in quadrant_table.items():
    print(f"{name}: {val}")
print("--------------------------------------------------")
