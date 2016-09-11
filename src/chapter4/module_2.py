# ファイル名: module_2.py
import module_1  # module_1をimportして内部のプログラムを実行


# module_1の内部の変数にアクセス
weight = module_1.wgt
# 以下、複数回にわたり、module_1の内部の関数にアクセス
module_1.teacher(weight)  # module_1の関数にアクセス
weight = module_1.run(weight)  # module_1の
module_1.teacher(weight)
