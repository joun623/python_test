def start_end_decorator(func):
    def new_function(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print(result)
        print("end")
        return result
    return new_function

@start_end_decorator
def twice(num):
    return num * num


twice(2)
