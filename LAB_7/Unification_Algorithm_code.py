import re

def parse_term(expr):
    expr = expr.replace(' ', '')  # Remove spaces
    tokens = re.findall(r'[A-Za-z0-9_]+|[(),]', expr)  # Tokenize expression

    def parse(tokens):
        if not tokens:
            return None
        token = tokens.pop(0)

        if token == '(':
            # Start of argument list
            args = []
            while tokens[0] != ')':
                args.append(parse(tokens))
                if tokens[0] == ',':
                    tokens.pop(0)  # Remove comma
            tokens.pop(0)  # Remove ')'
            return args
        elif re.match(r'[A-Za-z_][A-Za-z0-9_]*', token):
            if tokens and tokens[0] == '(':
                tokens.pop(0)  # Remove '('
                args = []
                while tokens[0] != ')':
                    args.append(parse(tokens))
                    if tokens[0] == ',':
                        tokens.pop(0)
                tokens.pop(0)  # Remove ')'
                return [token] + args
            else:
                return token
        else:
            return token

    return parse(tokens)

def is_variable(x):
    # Treat any single letter (upper or lowercase) as a variable
    return isinstance(x, str) and len(x) == 1 and x.isalpha()

def occurs_check(var, term, subst):
    # Prevents variable from being unified with itself or its own term
    if var == term:
        return True
    elif is_variable(term) and term in subst:
        return occurs_check(var, subst[term], subst)
    elif isinstance(term, list):
        return any(occurs_check(var, t, subst) for t in term)
    else:
        return False

def unify(x, y, subst=None):
    if subst is None:
        subst = {}
    x = substitute(x, subst)
    y = substitute(y, subst)

    if x == y:
        return subst
    if is_variable(x):
        return unify_var(x, y, subst)
    if is_variable(y):
        return unify_var(y, x, subst)
    if isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        if x[0] != y[0]:  # Ensure the function symbols match
            return None
        for xi, yi in zip(x[1:], y[1:]):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst
    return None

def unify_var(var, x, subst):
    # Prevent variable from unifying with itself or its own term
    if var in subst:
        return unify(subst[var], x, subst)
    elif is_variable(x) and x in subst:
        return unify(var, subst[x], subst)
    elif occurs_check(var, x, subst):
        return None
    else:
        subst[var] = x
        return subst

def substitute(term, subst):
    if isinstance(term, list):
        # When term is a function like ['f', 'Y'], make it into f(Y)
        return [term[0]] + [substitute(t, subst) for t in term[1:]]
    elif is_variable(term) and term in subst:
        return substitute(subst[term], subst)
    else:
        return term

def format_term(term):
    # If the term is a list (function), format it correctly
    if isinstance(term, list):
        return f"{term[0]}({', '.join(map(format_term, term[1:]))})"
    return term

# Input
expr1 = input("Enter first expression: ")  # e.g. p(b,X,f(g(Z)))
expr2 = input("Enter second expression: ") # e.g. p(z,f(Y),f(Y))

term1 = parse_term(expr1)
term2 = parse_term(expr2)

result = unify(term1, term2)

if result is None:
    print("No unifier exists.")
else:
    print("Most General Unifier (MGU):")
    for k, v in result.items():
        print(f"{k} = {format_term(v)}")
print("Samhitha A 1BM23CS293")
