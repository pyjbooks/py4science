# デコレータ（debug_log）の機能を有効にするためのフラグ
debug_trace = True
# 上記フラグが有効の場合、ログファイルを開く
if debug_trace:
    log_file = open("debug.log", "w", encoding='utf-8')


# デコレータ関数の定義
def debug_log(func):
    if debug_trace:
        def func_and_log(*args, **kwargs):
            # funcの実行前にログファイルに記録
            log_file.write("開始 %s: %s, %s\n" %
                           (func.__name__, args, kwargs))
            # funcをそのまま実行
            r = func(*args, **kwargs)
            # func終了時に再度ログファイルに記録
            log_file.write("終了 %s: 返り値 %s\n" % (func.__name__, r))
            return r
        return func_and_log
    else:
        return func  # debug_trace = False なら何も変えない


# デコレータでmyFuncの機能を変更
@debug_log
def myfunc(x):
    return x+x

# デコレータで変更後のmyFuncを実行
myfunc(3)
myfunc(5)
log_file.close()  # ログファイルを閉じる
