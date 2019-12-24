def decorator(func):
    def wrapper(*args, **kwargs):
        print("I'm a decorator")
        func()
    return wrapper


@decorator
def hello():
    print("I'm a function")


hello()
