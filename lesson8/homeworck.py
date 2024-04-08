import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function was done for {execution_time} second")
        return result
    return wrapper

def function(n):
    return sum(range(n))

sample_function = calculate_time(function)

result = sample_function(1000000)