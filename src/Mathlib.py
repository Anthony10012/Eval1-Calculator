from src.MathRequest import MathRequest

class Mathlib():

    def calculate(MathRequest):
        ope1= mathRequest.get_ope1()
        oper= mathRequest.get_oper()
        ope2= mathRequest.get_ope2()
        match oper:
            case '+':
                res = ope1 + ope2
            case '-':
                res = ope2 - ope2
            case '*':
                res = ope1 * ope2
            case '/':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return
                res = ope1 / ope2
            case _:
                print("Invalid operator.")
                return
        return res






