from src.MathRequest import MathRequest

class Mathlib:
    @classmethod
    def execute(self, mathRequest):
        oper= mathRequest.get_oper()
        ope1 =mathRequest.get_ope1()
        ope2 =mathRequest.get_ope2()

        match mathRequest.get_oper() :
            case 'add':
                mathRequest.set_res(mathRequest.get_ope1() + mathRequest.get_ope2())

            case 'sub':
                mathRequest.set_res(mathRequest.get_ope1() - mathRequest.get_ope2())

            case 'div':
                mathRequest.set_res(mathRequest.get_ope1() / mathRequest.get_ope2())

            case 'mul':
                mathRequest.set_res(mathRequest.get_ope1() * mathRequest.get_ope2())


