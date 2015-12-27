def exhaustion(times, input_string):
    if 1 == times:
        return input_string
    return [x + y for x in input_string for y in exhaustion(times - 1, input_string)]


def combine_to_expression(numbers, operators):
    if len(operators) >= len(numbers):
        raise ValueError('numbers size should greater than operators')
    result = ''
    for count in range(len(numbers + operators)):
        if count % 2 == 1:
            operators, operator = operators[1:], operators[0]
            result += operator
        else:
            numbers, number = numbers[1:], numbers[0]
            result += number
    return result


def generate_all_expressions(number_list, operator_list):
    return [combine_to_expression(number, operator) for number in number_list for operator in operator_list]


if '__main__' == __name__:
    print(exhaustion(4, '1234'))
    print(exhaustion(3, '+-*/'))
    print(combine_to_expression('1234', '*-+'))
    print(generate_all_expressions(exhaustion(2, '12'), exhaustion(1, '+')))
