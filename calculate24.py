import math


def exhaustion_exponential(n, input_string):
    """generate all exponential(n) combination with input_string
    Args:
        n: (int) how many time should be run
        input_string: (str)
    Returns:
        set of str
    """
    if 1 == n:
        return input_string
    return [x + y for x in input_string for y in exhaustion_exponential(n - 1, input_string)]


def exhaustion_factorial(source_string):
    """generate all factorial(n!, n = len(source_string)) combination with source_string
    Args:
        source_string: (str)
    Returns:
        list of str
    """
    if 1 == len(source_string):
        return [source_string]
    # remove character which position equal index from source_string and put to next recursion
    return [x + y for index, x in enumerate(source_string) for y in
            exhaustion_factorial(''.join([source_string[i] for i in range(len(source_string)) if i != index]))]


def calculate_with_postfix_string(expression):
    """calculate with postfix string
    Args:
        expression: (str) format is postfix
    Returns:
        (int) result of input expression, floating result will ceil to integer
    Raises:
        IndexError when there are not supported operator
    """
    operator_map = {'+': lambda *val: val[0] + val[1],
                    '-': lambda *val: val[0] - val[1],
                    '*': lambda *val: val[0] * val[1],
                    '/': lambda *val: val[0] / val[1] if 0 != val[1] else None}
    operand_stack = []
    for element in expression:
        try:
            # it is integer
            operand_stack.append(int(element))
        except ValueError:
            # it is operator
            if len(operand_stack) >= 2:
                if element not in operator_map:
                    raise IndexError('Not supported operator', element)
                r = operator_map[element](*operand_stack[-2:])
                if r is None:
                    return None
                operand_stack = operand_stack[:-2]
                operand_stack.append(r)
            else:
                return None
    if len(operand_stack) != 1:
        return None
    return math.ceil(operand_stack.pop())


def calculate24(operands):
    operators = '+-*/'
    operators_combination = exhaustion_exponential(len(operands) - 1, operators)
    component_combination = [operands + operators_ele for operators_ele in operators_combination]
    # print(component_combination)
    operator_combination = map(exhaustion_factorial, component_combination)
    for expression_list in operator_combination:
        for expression in expression_list:
            if 24 == calculate_with_postfix_string(expression):
                print(expression, end=', ')


if '__main__' == __name__:
    print(exhaustion_exponential(4, '1234'))
    print(exhaustion_exponential(3, '+-*/'))
    calculate24('1234')