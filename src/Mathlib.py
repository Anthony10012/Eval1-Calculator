from src.MathRequest import MathRequest

class Mathlib:
    @classmethod
    def execute(self, mathRequest):
        match mathRequest.get_oper() :
            case 'add':
                mathRequest.set_res(mathRequest.get_ope1() + mathRequest.get_ope2())








