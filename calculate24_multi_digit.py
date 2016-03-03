from fractions import Fraction
from calculate24 import calculate_with_postfix
from calculate24 import postfix_to_infix


def list_all_exponential_permutation(n, inputs):
    # 輸入: 由int + str組成的list
    # 輸出: list of list, 指數排列組合
    if 1 == n:
        return [[x] for x in inputs]
    final_result = []
    for element in inputs:
        results = list_all_exponential_permutation(n - 1, inputs)
        for a_result in results:
            a_result.insert(0, element)
        final_result += results
    return final_result


def list_all_factorial_permutation(components):
    # 輸入: int + str(+-*/) 的 list, 個數都是0~多個
    # 輸出: int與str的所有排列組合
    if 1 == len(components):
        return [components]
    final_result = []
    for element in components:
        temp_components = list(components)
        temp_components.remove(element)
        results = list_all_factorial_permutation(temp_components)
        for sub_result in results:
            if len(sub_result) >= len(components):
                continue
            assert isinstance(sub_result, list)
            sub_result.insert(0, element)
        final_result += results
    return final_result


def calculate24(operands):
    operators = '+-*/'
    operators_combination = list_all_exponential_permutation(len(operands) - 1, operators)
    component_combination = [operands + operators_ele for operators_ele in operators_combination]
    operator_combination = map(list_all_factorial_permutation, component_combination)
    result_expression = []
    for expression_list in operator_combination:
        for expression in expression_list:
            if Fraction(24) == calculate_with_postfix(expression) and expression not in result_expression:
                result_expression.append(expression)
    return result_expression

if '__main__' == __name__:
    print(list_all_factorial_permutation([11, 22, '3', '+']))
    print(calculate_with_postfix([1, 2, 3, 4, '*', '*', '*']))
    print(list(map(postfix_to_infix, calculate24([3, 3, 8, 8]))))
    # print(list(map(postfix_to_infix, calculate24([1, 2, 3, 4]))))
