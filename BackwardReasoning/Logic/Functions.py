from .LiurcaDaniel27Representation import *

def evaluate_function(func):
    func_args = []

    for arg in get_args(func):
        if is_constant(arg):
            func_args.append(get_value(arg))
        elif is_variable(arg):
            return None
        elif is_function_call(arg):
            func_args.append(evaluate_function(arg))

    return globals()[get_head(func)](*func_args)


def get(triangle, side):
    if side == '0':
        return triangle[:2]

    if side == '1':
        return triangle[0] + triangle[2]

    if side == '2':
        return triangle[1:]

    return None


def compute_triangle(L1, L2, L3):
    maxim = max(int(L1), int(L2), int(L2))

    if int(L1) == maxim:
        return str(int(L2) + int(L3) - int(L1))

    if int(L2) == maxim:
        return str(int(L1) + int(L3) - int(L2))

    if int(L3) == maxim:
        return str(int(L1) + int(L2) - int(L3))


def getShortest(L1, L2, L3):
    return str(sorted([int(L1), int(L2), int(L3)])[0])


def getMiddle(L1, L2, L3):
    return str(sorted([int(L1), int(L2), int(L3)])[1])


def getLongest(L1, L2, L3):
    return str(sorted([int(L1), int(L2), int(L3)])[2])


def compute_pitagoras(LS, LM, LL):
    return str(int(LS) * int(LS) + int(LM) * int(LM) - int(LL) * int(LL))