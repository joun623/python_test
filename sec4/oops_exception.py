class OopsException(Exception):
    pass

try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)
