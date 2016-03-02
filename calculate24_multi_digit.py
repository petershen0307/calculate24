from fractions import Fraction


def list_all_exponential_permutation(n, inputs):
    # 輸入: 由int + str組成的list
    # 輸出: list of list, 指數排列組合
    if 1 == n:
        return [inputs]
    return None


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


if '__main__' == __name__:
    print(list_all_factorial_permutation([11, 22, '3', '+']))
