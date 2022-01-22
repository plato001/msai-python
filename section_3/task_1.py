def calc_arithmetic_expression(s):
    try:
        num_1, operator_, num_2 = s.split()
        num_1, num_2 = map(float, [num_1, num_2])
        if operator_ not in ["+", "-", "*", "/"]:
            raise ValueError
        if operator_ == "+":
            return num_1 + num_2
        elif operator_ == "-":
            return num_1 - num_2
        elif operator_ == "*":
            return num_1 * num_2
        elif operator_ == "/":
            try:
                return num_1 / num_2
            except ZeroDivisionError:
                return "Error! Division by zero!"
    except ValueError:
        return "Error of input format! You should enter 'number operator number'"


if __name__ == '__main__':
    input_ = input()
    print(calc_arithmetic_expression(input_))
