# クラスCoeffVarを定義
class CoeffVar(object):
    coefficient = 1

    @classmethod  # メソッドmulをクラスメソッド化
    def mul(cls, fact):  # 第1引数はcls
        return cls.coefficient * fact


# クラスCoeffvarを継承するクラスMulFiveを定義
class MulFive(CoeffVar):
    coefficient = 5


x = MulFive.mul(4)  # CoeffVar.mul(MulFive, 4) -> 20
