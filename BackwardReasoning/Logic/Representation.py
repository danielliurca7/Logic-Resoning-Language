def make_const(value):
    return ('constant', value)

def make_var(name):
    return ('variable', name)

def make_function_call(function, *args):
    return ('function', function, list(args))

def make_atom(predicate, *args):
    return ('atom', predicate, list(args), 1)

def make_neg(sentence):
    return ('negation', [sentence])

def make_and(sentence1, sentence2, *others):
    return ('and', [sentence1, sentence2] + list(others))

def make_or(sentence1, sentence2, *others):
    return ('or', [sentence1, sentence2] + list(others), 1)

def replace_args(formula, new_args):
    if is_function_call(formula) or is_atom(formula):
        formula = (formula[0], formula[1], new_args)
    elif is_sentence(formula):
        formula = (formula[0], new_args)
        
    return formula

def replace_atom_cf(formula, cf):
    if is_atom(formula):
        return (formula[0], formula[1], formula[2], cf)
    elif is_sentence(formula):
        return (formula[0], formula[1], cf)
    else:
        return None

    
    
def is_term(f):
    return is_constant(f) or is_variable(f) or is_function_call(f)

def is_constant(f):
    return f[0] == 'constant'

def is_variable(f):
    return f[0] == 'variable'

def is_function_call(f):
    return f[0] == 'function'

def is_atom(f):
    return f[0] == 'atom'

def is_sentence(f):
    return is_atom(f) or f[0] == 'negation' or f[0] == 'and' or f[0] == 'or'

def has_args(f):
    return is_function_call(f) or is_sentence(f)



def get_value(f):
    return f[1] if is_constant(f) else None

def get_name(f):
    return f[1] if is_variable(f) else None

def get_head(f):
    if f[0] == 'negation':
        return '~'
    elif f[0] == 'and':
        return 'A'
    elif f[0] == 'or':
        return 'v'
    return f[1] if is_function_call(f) or is_atom(f) else None

def get_args(f):
    return f[2] if is_function_call(f) or is_atom(f) else f[1] if is_sentence(f) else None

def get_cf(f):
    return f[3] if is_atom(f) else f[2] if is_sentence(f) else None



def is_positive_literal(L):
    return is_atom(L)

def is_negative_literal(L):
    return get_head(L) == '~' and is_positive_literal(get_args(L)[0])

def is_literal(L):
    return is_positive_literal(L) or is_negative_literal(L)



def get_premises(formula):
    premises = []
    
    for arg in get_args(formula):
        if is_negative_literal(arg):
            premises.append(get_args(arg)[0])
    
    return premises

def get_conclusion(formula):
    for arg in get_args(formula):
        if is_positive_literal(arg):
            return arg

def is_fact(formula):
    return is_positive_literal(formula)

def is_rule(formula):
    return get_head(formula) == 'v' or get_head(formula) == 'A'



def equal_terms(t1, t2):
    if is_constant(t1) and is_constant(t2):
        return get_value(t1) == get_value(t2)
    if is_variable(t1) and is_variable(t2):
            return get_name(t1) == get_name(t2)
    if is_function_call(t1) and is_function_call(t2):
        if get_head(t1) != get_head(t2):
            return all([equal_terms(get_args(t1)[i], get_args(t2)[i]) for i in range(len(get_args(t1)))])
    return False

def is_equal_to(a1, a2):
    if not (is_atom(a1) and is_atom(a2) and get_head(a1) == get_head(a2) and len(get_args(a1)) == len(get_args(a2))):
        return False
    return all([equal_terms(get_args(a1)[i], get_args(a2)[i]) for i in range(len(get_args(a1)))])



def print_formula(f, return_result = False):
    ret = ""
    if is_term(f):
        if is_constant(f):
            ret += str(get_value(f))
        elif is_variable(f):
            ret += "?" + get_name(f)
        elif is_function_call(f):
            ret += str(get_head(f)) + "[" + "".join([print_formula(arg, True) + "," for arg in get_args(f)])[:-1] + "]"
        else:
            ret += "???"
    elif is_atom(f):
        ret += str(get_head(f)) + "(" + "".join([print_formula(arg, True) + ", " for arg in get_args(f)])[:-2] + ")"
    elif is_sentence(f):
        args = get_args(f)
        if len(args) == 1:
            ret += str(get_head(f)) + print_formula(args[0], True)
        else:
            ret += "(" + str(get_head(f)) + "".join([" " + print_formula(arg, True) for arg in get_args(f)]) + ")"
    else:
        ret += "???"
    if return_result:
        return ret
    print(ret)
    return



def add_statement(kb, conclusion, cf, *hypotheses):
    s = replace_atom_cf(conclusion, cf) \
        if not hypotheses \
        else replace_atom_cf(make_or(*([make_neg(s) for s in hypotheses] + [conclusion])), cf)

    kb.append(s)