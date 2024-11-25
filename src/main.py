operand1 = float
operator = None
operand2 = float

def main():
    ask_user_input()
    result = calculate(float(), operator,float(operand2))
    display_result(float(operand1), operator, float(operand2), float(result))
    ask_user_float_input(float)


def ask_user_float_input():
    global operand1
    operand1 = ask_user_float_input("Enter the first operand: ")

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    global operand2
    # Get second operand from the user
    operand2 = ask_user_float_input("Enter the second operand: ")


def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = ask_user_float_input("Enter the first operand: ")

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    global operand2
    # Get second operand from the user
    operand2 = ask_user_float_input("Enter the second operand: ")

def calculate(ope1, oper, ope2):
    # Perform the operation based on the operator
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
 # Fonction puissance
    def maFonction(n):
        somme = 1
        for count in range(int(n)):
            somme = somme * 2
        return somme

    # Ce print sert à tester la fonction
    print(maFonction(3))


def display_result(op1, ope, ope2, res):
    print(float(op1) + " " + ope + " " + float(ope2) + " = " + float(res))


# Call the main function to run the program
main()