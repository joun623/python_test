def safe_division(number, divisor,*, ignore_overflow=False,
        ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

def main():
    print(safe_division(1, 0, ignore_zero_division=True) )

main()
