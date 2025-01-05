import math

class ScientificCalculator:
    def __init__(self):
        self.memory = 0  # For storing a value in memory

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def sqrt(self, num):
        if num < 0:
            raise ValueError("Square root of negative number is not allowed.")
        return math.sqrt(num)

    def factorial(self, num):
        if not num.is_integer() or num < 0:
            raise ValueError("Factorial is defined for non-negative integers only.")
        return math.factorial(int(num))

    def sin(self, angle):
        return math.sin(math.radians(angle))

    def cos(self, angle):
        return math.cos(math.radians(angle))

    def tan(self, angle):
        return math.tan(math.radians(angle))

    def log(self, num, base=10):
        if num <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers.")
        return math.log(num, base)

    def ln(self, num):
        if num <= 0:
            raise ValueError("Natural logarithm is not defined for non-positive numbers.")
        return math.log(num)

    def store_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0


def main():
    calc = ScientificCalculator()
    print("Welcome to the Scientific Calculator!")
    print("Type 'help' for the list of commands or 'exit' to quit.\n")

    while True:
        try:
            user_input = input("Enter command: ").strip().lower()
            if user_input == "exit":
                print("Goodbye!")
                break
            elif user_input == "help":
                print("""
Available Commands:
- add a b         : Addition
- subtract a b    : Subtraction
- multiply a b    : Multiplication
- divide a b      : Division
- power a b       : Exponentiation (a^b)
- sqrt a          : Square root
- factorial a     : Factorial
- sin a           : Sine of angle (in degrees)
- cos a           : Cosine of angle (in degrees)
- tan a           : Tangent of angle (in degrees)
- log a b         : Logarithm (base b)
- ln a            : Natural logarithm
- store a         : Store value in memory
- recall          : Recall value from memory
- clear           : Clear memory
- exit            : Quit the calculator
                """)
            else:
                parts = user_input.split()
                command = parts[0]
                args = list(map(float, parts[1:]))

                if command == "add":
                    print(calc.add(*args))
                elif command == "subtract":
                    print(calc.subtract(*args))
                elif command == "multiply":
                    print(calc.multiply(*args))
                elif command == "divide":
                    print(calc.divide(*args))
                elif command == "power":
                    print(calc.power(*args))
                elif command == "sqrt":
                    print(calc.sqrt(*args))
                elif command == "factorial":
                    print(calc.factorial(*args))
                elif command == "sin":
                    print(calc.sin(*args))
                elif command == "cos":
                    print(calc.cos(*args))
                elif command == "tan":
                    print(calc.tan(*args))
                elif command == "log":
                    print(calc.log(*args))
                elif command == "ln":
                    print(calc.ln(*args))
                elif command == "store":
                    calc.store_memory(args[0])
                    print("Value stored in memory.")
                elif command == "recall":
                    print("Memory value:", calc.recall_memory())
                elif command == "clear":
                    calc.clear_memory()
                    print("Memory cleared.")
                else:
                    print("Unknown command. Type 'help' for a list of commands.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
