# Muhammad Mujtaba
# CS-117; 540040
# 2k25 BESE-16B
from math import sqrt
from typing import Callable
from dataclasses import dataclass


# make sure "1.0" is printed as "1" and "1.5" as "1.5"
def sanitize_num(_number: type[int] | type[float]) -> float | int:
    return int(_number) if int(_number) == float(_number) else float(_number)


# input a number; cast it to required type; check if in range
def safe_input_num(
    cast_type: type[int] | type[float],  # can be int OR float
    message: str,
    min=None,
    max=None,
    error_callback=lambda: None,  # called on error; Optional
):
    # for developer only
    if not cast_type is int and not cast_type is float:
        raise TypeError(
            f"Type of cast_type can be either float or int given: {cast_type.__name__}"
        )

    # loop until user enters valid value
    while True:
        result = None
        try:
            result = cast_type(input(message))
            # check range
            if min is not None and (result or 0) < min:
                raise
            if max is not None and (result or 0) > max:
                raise
            return result
        except:
            # print errors to the user
            if min is not None and (result or 0) < min:
                print(
                    f"PLEASE INPUT A VALID {cast_type.__name__.upper()} MORE THAN {str(min)}"
                )
            elif max is not None and (result or 0) > max:
                print(
                    f"PLEASE INPUT A VALID {cast_type.__name__.upper()} LESS THAN {str(max)}"
                )
            elif min is not None and max is not None:
                print(
                    f"PLEASE INPUT A VALID {cast_type.__name__.upper()} BETWEEN {str(min)} AND {str(max)}"
                )
            else:
                print(f"PLEASE INPUT A VALID {cast_type.__name__.upper()}")

            error_callback()

            # not necessary added for readability
            continue  # user didn't input valid value rerun loop


# list of all functions grouped for convienience
class OperationsList:
    # catching any random error using a decorator
    # sometimes called when very large number is exponentiated
    def error_handler(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return None

        # renaming functoin : IMPORTANT
        wrapper.__name__ = func.__name__
        return wrapper

    @staticmethod
    @error_handler
    def addition(a: float, b: float) -> float | None:
        return a + b

    @staticmethod
    @error_handler
    def subtraction(a: float, b: float) -> float | None:
        return a - b

    @staticmethod
    @error_handler
    def multiplication(a: float, b: float) -> float | None:
        return a * b

    @staticmethod
    @error_handler
    def division(a: float, b: float) -> float | None:
        return a / b if b != 0 else None

    @staticmethod
    @error_handler
    def exponentiation(a: float, b: float) -> float | None:
        return a**b

    @staticmethod
    @error_handler
    def root(a: float, b: float) -> float | None:
        return a ** (1 / b) if b != 0 else None

    @staticmethod
    @error_handler
    def sqrt(a: float, _: float) -> float | None:
        return sqrt(a)

    @staticmethod
    @error_handler
    def is_even(a: float, _: float) -> float | None:
        return a % 2

    @staticmethod
    @error_handler
    def percentage(obtained: float, total: float) -> float | None:
        return (obtained / total) * 100 if total != 0 else None


# convienience for printing the operators in format in terminal
class OperationsPrint:
    @staticmethod
    def addition(a: float, b: float, result: float | None) -> str:
        return f"{a} + {b} = {result}"

    @staticmethod
    def subtraction(a: float, b: float, result: float | None) -> str:
        return f"{a} - {b} = {result}"

    @staticmethod
    def multiplication(a: float, b: float, result: float | None) -> str:
        return f"{a} * {b} = {result}"

    @staticmethod
    def division(a: float, b: float, result: float | None) -> str:
        return f"{a} / {b} = {result}"

    @staticmethod
    def exponentiation(a: float, b: float, result: float | None) -> str:
        return f"{a} ^ {b} = {result}"

    @staticmethod
    def root(a: float, b: float, result: float | None) -> str:
        return f"{b} root {a} = {result}"

    @staticmethod
    def sqrt(a: float, _, result: float | None) -> str:
        return f"sqrt({a}) = {result}"

    @staticmethod
    def is_even(a: float, _, result: float | None) -> str:
        return f"{a} is {'even' if result == 0 else 'odd'}"

    @staticmethod
    def percentage(obtained: float, total: float, result: float | None) -> str:
        return f"{obtained} is {result}% of {total}"


# analagous to struct in C++
@dataclass
class Operation:
    id: int
    func: Callable[[float, float], float]
    symbol: str
    print_func: Callable[[float, float, float], str]
    is_mono_input: bool = False


# list of operations
OPERATIONS = [
    Operation(1, OperationsList.addition, "+", OperationsPrint.addition),
    Operation(2, OperationsList.subtraction, "-", OperationsPrint.subtraction),
    Operation(3, OperationsList.multiplication, "*", OperationsPrint.multiplication),
    Operation(4, OperationsList.division, "/", OperationsPrint.division),
    Operation(5, OperationsList.exponentiation, "^", OperationsPrint.exponentiation),
    Operation(6, OperationsList.percentage, "%", OperationsPrint.percentage),
    Operation(7, OperationsList.root, "ROOT", OperationsPrint.root),
    Operation(8, OperationsList.sqrt, "SQRT", OperationsPrint.sqrt, is_mono_input=True),
    Operation(
        9, OperationsList.is_even, "EVEN", OperationsPrint.is_even, is_mono_input=True
    ),
]


# function to print all operations in list
def print_operations():
    print(" ")
    print("Available Operations:")
    for op in OPERATIONS:
        print(f"{op.id}: \t{op.func.__name__.capitalize()} \t\t{op.symbol}")
    print(" ")


# make sure the code always run when this is executable
# analagous to main function in C++
if __name__ == "__main__":
    # LOOP FLOW
    # print operations
    # get operation from user
    # get inputs form user
    # print output of operation
    # ask user if wants to repeat

    while True:
        # 1. print operations
        print_operations()
        # 2. get operation from user
        op_input = safe_input_num(
            int,
            "Input operation to perform: ",
            min([op.id for op in OPERATIONS]), # using python utils provided in library
            max([op.id for op in OPERATIONS]), # using python utils provided in library
            error_callback=lambda: print_operations(),
        )

        # 3. get inputs form user
        selected_op = next(op for op in OPERATIONS if op.id == op_input)
        # if mono_input i.e requres one input only handle accordingly
        a = safe_input_num(float, f"Enter {'the' if selected_op.is_mono_input else '1st'} number: ")
        b = 0.0 if selected_op.is_mono_input else safe_input_num(float, "Enter 2nd number: ")

        # 4. print output of operation
        
        # formatting output
        # perform operation using struct
        result = selected_op.func(a, b)
        if result is None:
            print("ERROR: restarting")
            continue
        # round to 3 decimal places
        result = round(result, 3)
        # print using print utility in struct
        print(f"{selected_op.print_func(a, b, result)}")

        # 5. ask user if wants to repeat
        # press enter to continue else to break
        cont = input("Press ENTER to continue or any OTHER key then ENTER to exit: ")
        if cont != "":
            print("Exiting...")
            break
