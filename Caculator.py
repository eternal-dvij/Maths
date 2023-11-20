class Calculator:
    """
    A simple calculator class that supports basic arithmetic operations.

    Methods:
    - add(*values: int): Performs addition on the provided values and prints the result.
    - subtract(*values: int): Performs subtraction on the provided values and prints the result.
    - multiply(*values: int): Performs multiplication on the provided values and prints the result.
    - divide(*values: int): Performs division on the provided values and prints the result.

    Example:
    calculator = Calculator()
    calculator.add(2, 3, 5)  # Output: Sum of [2, 3, 5] is: 10
    calculator.subtract(10, 2, 3)  # Output: Subtraction of [10, 2, 3] is: 5
    calculator.multiply(2, 3, 4)  # Output: Multiplication of [2, 3, 4] is: 24
    calculator.divide(100, 5, 2)  # Output: Division of [100, 5, 2] is: 10
    """

    def add(self, *values: int):
        """
        Performs addition on the provided values and prints the result.

        Parameters:
        - values: Variable number of integers to be added.

        Example:
        calculator.add(2, 3, 5)  # Output: Sum of [2, 3, 5] is: 10
        """
        x = list(values)
        print(f'Sum of {x} is=: {sum(values)}')

    def subtract(self, *values: int):
        """
        Performs subtraction on the provided values and prints the result.

        Parameters:
        - values: Variable number of integers to be subtracted.

        Example:
        calculator.subtract(10, 2, 3)  # Output: Subtraction of [10, 2, 3] is: 5
        """
        x = list(values)
        result = values[0]
        if len(values) > 1:
            for i in values[1:]:
                result -= i
            print(f'Subtraction of {x} is: {result}')
        else:
            print(f'Subtraction of {x} is: {result}')

    def multiply(self, *values: int):
        """
        Performs multiplication on the provided values and prints the result.

        Parameters:
        - values: Variable number of integers to be multiplied.

        Example:
        calculator.multiply(2, 3, 4)  # Output: Multiplication of [2, 3, 4] is: 24
        """
        x = list(values)
        result = values[0]
        if len(values) > 1:
            for i in values[1:]:
                result *= i
            print(f'Multiplication of {x} is: {result}')
        else:
            print(f'Multiplication of {x} is: {result}')

    def divide(self, *values: int):
        """
        Performs division on the provided values and prints the result.

        Parameters:
        - values: Variable number of integers to be divided.

        Example:
        calculator.divide(100, 5, 2)  # Output: Division of [100, 5, 2] is: 10
        """
        x = list(values)
        result = values[0]
        if len(values) > 1:
            for i in values[1:]:
                result /= i
            print(f'Division of {x} is: {int(result)}')
        else:
            print(f'Division of {x} is: {int(result)}')
