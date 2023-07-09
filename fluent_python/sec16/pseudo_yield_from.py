# RESULT = yield from EXPRの擬似コード

_i = ITER(EXPR)
try: 
    _y = next(_i)
    # 初期化処理まで
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break
Result = _r

# 様々な状況に対応したバージョン
_i = ITER(EXPR)
try: 
    _y = next(_i)
    # 初期化処理まで
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _i.send(_s)
        except GeneratorExit as _e:
            try:
                # closeが実装されていない場合もある
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e

        except BaseException as _e:
            # throwで投げてきた例外処理
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break

        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
Result = _r


