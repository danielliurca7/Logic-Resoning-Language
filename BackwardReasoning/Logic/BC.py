from copy import deepcopy

from .LiurcaDaniel27Representation import *
from .LiurcaDaniel27Unification import *
from .LiurcaDaniel27Functions import *


def print_level(text, level, verbose):
    if verbose:
        print('\t' * level + text)


def has_variables(atom):
    args = get_args(atom)
    
    for arg in args:
        if is_variable(arg):
            return True
        
    return False


def has_substitution(subst_list):
    for subst in subst_list:
        if subst is not False:
            return True
        
    return False


def natural_join(subst1, subst2):
    if not subst1:
        return subst2

    if not subst2:
        return subst1

    new_subst = []

    for s1 in subst1:
        for s2 in subst2:
            if s1[0] is True:
                new_subst.append((s2[0], s1[1]))
            elif s2[0] is True:
                new_subst.append((s1[0], s2[1]))
            else:
                common_vars = s1[0].keys() & s2[0].keys()
                
                is_mergeable = True

                for var in common_vars:
                    if s1[0][var] != s2[0][var]:
                        is_mergeable = False

                if is_mergeable:
                    s3 = ({**s1[0], **s2[0]}, min(s1[1], s2[1]))
                    new_subst.append(s3)

    return new_subst


def backward_chaining(kb, theorem, level = 0, verbose = True):
    # if top level query copy knowledge base
    # else use knowledge base of the parent
    if level == 0:
        local_kb = deepcopy(kb)
    else:
        local_kb = kb

    new_args = []

    # evaluate the functions inside theorem arguments
    for arg in get_args(theorem):
        if is_function_call(arg):
            new_args.append(make_const(evaluate_function(arg)))
        else:
            new_args.append(arg)

    theorem = replace_args(theorem, new_args)

    print_level('Theorem to prove ' + print_formula(theorem, True), level, verbose)

    # if the theorem contains only constants as arguments
    # search it in the knowledge base
    if not has_variables(theorem):
        for fact in filter(is_fact, local_kb):
            subst = unify(fact, theorem)

            if subst is not False:
                print_level('Fact found in KB: ' + print_formula(theorem, True) + ' with confidece factor ' + str(get_cf(fact)), level + 1, verbose)
                return (True, get_cf(fact))
        
    subst_list = []

    # if the theorem contains variables as arguments
    # search facts that unifies with the theorem
    for fact in filter(is_fact, local_kb):
        subst = unify(fact, theorem)

        if subst is not False:
            print_level('Fact found in KB: ' + print_formula(fact, True) + ' with confidece factor ' + str(get_cf(fact)), level + 1, verbose)

            theorem_vars = [get_name(var) for var in get_args(theorem) if is_variable(var)]

            theorem_subst = {k : v for k, v in subst.items() if k in theorem_vars}

            if theorem_subst:
                subst_list.append((theorem_subst, get_cf(fact)))
            else:
                subst_list.append((True, get_cf(fact)))

    to_delete = []

    # if the theorem contains variables as arguments
    # search rules with a conclusion that unifies with the theorem
    for rule in filter(is_rule, local_kb):
        # make sure variables in theorem have different names than variables in rule
        unique_var_theorem = make_atom(theorem[1], *[make_var('?' + get_name(arg)) if is_variable(arg) else arg for arg in get_args(theorem)])

        subst = unify(get_conclusion(rule), unique_var_theorem)

        if subst is not False:
            delete = False

            conclusion = substitute(get_conclusion(rule), subst)

            print_level('Found applicable rule in KB: ' + print_formula(get_conclusion(rule), True) + ' :- ' +
                        ' , '.join([print_formula(premise, True) for premise in get_premises(rule)]) +
                        ' with confidence ' + str(round(get_cf(rule), 3)), level + 1, verbose)
            premise_subst = []

            # for every premise            
            for premise in get_premises(rule):
                new_substs = []
                subst_to_remove = []

                # if there are substitutions in the current substitution list
                # try to unify the current premise with every substitution in the current substitution listF
                if premise_subst:
                    for s in premise_subst:
                        new_subst = backward_chaining(kb, substitute(substitute(premise, subst), s[0]), level + 2, verbose)

                        if new_subst[0] is False:
                            subst_to_remove.append(s)
                        elif new_subst[0] is True:
                            new_substs += [(s[0], s[1])]
                        elif new_subst[0] is not True:
                            # get only the variables that appear in the current premise from the substitution
                            premise_vars = [get_name(statement) for statement in get_args(substitute(substitute(premise, subst), s)) if is_variable(statement)]                        
                            new_subst = [({k : v for k, v in subst[0].items() if k in premise_vars} if isinstance(subst[0], dict) else subst[0], subst[1]) for subst in new_subst]
                            new_substs += natural_join([s], new_subst)
                else:
                    new_subst = backward_chaining(kb, substitute(premise, subst), level + 2, verbose)

                    if new_subst[0] is False:
                        break
                    elif new_subst[0] is True:
                        new_substs += [(subst, new_subst[1])]
                    elif new_subst[0] is not True:
                        # get only the variables that appear in the current premise from the substitution
                        premise_vars = [get_name(statement) for statement in get_args(substitute(premise, subst)) if is_variable(statement)]
                        new_subst = [({k : v for k, v in subst[0].items() if k in premise_vars} if isinstance(subst[0], dict) else subst[0], subst[1]) for subst in new_subst]
                        new_substs += natural_join([(subst, get_cf(rule))], new_subst)

                # remove the sustitutions that don't unify with the current premise
                for s in subst_to_remove:
                    premise_subst.remove(s)

                # join the substitutions
                premise_subst = natural_join(premise_subst, new_substs)

            # if no substitutions we try the next rule
            if premise_subst == []:
                continue

            # get the variables in the conclusion
            conclusion_vars = [get_name(var) for var in get_args(conclusion) if is_variable(var)]

            # get only the variables that appear in the conclusion from the substitution
            for subst in premise_subst:
                conclusion_subst = {k[1:] : v for k, v in subst[0].items() if k in conclusion_vars}

                if conclusion_subst:
                    subst_list.append((conclusion_subst, subst[1] * get_cf(rule)))
                else:
                    subst_list.append((True, subst[1] * get_cf(rule)))

                if len(conclusion_vars) == len(get_args(conclusion)):
                    delete = True
                    add_statement(local_kb, substitute(conclusion, subst), 1)

            if delete: to_delete.append(rule)

            if subst_list:
                for subst in subst_list:
                    print_level('Solution found for rule ' + print_formula(get_conclusion(rule), True) + ' :- ' +
                                ' , '.join([print_formula(premise, True) for premise in get_premises(rule)]) + ' : ' +
                                (' ; '.join([s + ' : ' + get_value(subst[0][s]) for s in subst[0]]) if isinstance(subst[0], dict) else str(subst[0])) +
                                ' with confidence factor ' + str(round(subst[1], 3)), level + 1, verbose)

    # as an optimisation if we calculate all the possible substitutions for a rule
    # we add the conclusion with those substitutions as fact and we delete the rule
    for rule in to_delete:
        local_kb.remove(rule)

    # if we didn't find any substitutions that unify return False
    if not subst_list:
        print_level('No solution found for theorem ' + print_formula(theorem, True), level, verbose)
        return (False, 0.0)
    else:
        for subst in subst_list:
            print_level('Solution found for theorem ' + print_formula(theorem, True) + ': ' +
                        (' ; '.join([s + ' : ' + get_value(subst[0][s]) for s in subst[0]]) if isinstance(subst[0], dict) else str(subst[0])) +
                        ' with confidence factor ' + str(round(subst[1], 3)), level, verbose)

    subst_set = []

    for subst in subst_list:
        subs = [s for s in subst_list if s[0] == subst[0]]

        if subst[0] not in [s[0] for s in subst_set]:
            current_cf = 0

            for s in subs:
                x = current_cf
                y = s[1]

                if x > 0 and y > 0:
                    current_cf = x + y - x * y
                elif x < 0 and y < 0:
                    current_cf = x + y + x * y
                else:
                    current_cf = (x + y) / (1 - min(abs(x), abs(y)))

            subst_set.append((subst[0], round(current_cf, 3)))

    return subst_set