import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Execution time: {execution_time}')
        return result
    return wrapper

def debugger(func):
    def wrapper(*args, **kwargs):
        print(f'Calling function {func.__name__} with arguments args: {args} and kwargs {kwargs}...')
        result = func(*args, **kwargs)
        print(f'Function return is {result}')
        return result
    return wrapper
