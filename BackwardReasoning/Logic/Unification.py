from copy import deepcopy

from .LiurcaDaniel27Representation import *

def substitute(f, substitution):
    if substitution is None:
        return None
    if is_variable(f) and (get_name(f) in substitution):
        return substitute(substitution[get_name(f)], substitution)
    if has_args(f):
        return replace_args(f, [substitute(arg, substitution) for arg in get_args(f)])
    return f


def occur_check(v, t, subst):
    if v == t:
        return True
    elif get_name(t) in subst:
        return occur_check(v, substitute(t, subst), subst)
    elif is_function_call(t):
        for arg in get_args(t):
            if occur_check(v, arg, subst):
                return True

    return False



def unify(f1, f2, subst = None):
    if subst is None:
        subst = {}
    S = []
    S.append((f1, f2))
    
    while len(S) > 0:
        s, t = S.pop()
        
        while get_name(s) in subst:
            s = substitute(s, subst)
        while get_name(t) in subst:
            t = substitute(t, subst)
            
        if s != t:
            if is_variable(s):
                if occur_check(s, t, subst):
                    return False
                else:
                    subst[get_name(s)] = t
            elif is_variable(t):
                if occur_check(t, s, subst):
                    return False
                else:
                    subst[get_name(t)] = s
            elif has_args(s) and has_args(t):
                if get_head(s) == get_head(t) and len(get_args(s)) == len(get_args(t)):
                    for i in range(len(get_args(s))):
                        S.append((get_args(s)[i], get_args(t)[i]))        
                else:
                    return False
            else:
                return False
                    
    return subst