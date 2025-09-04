# 4. Dynamic Argument Logger
def log_args_kwargs(*args, **kwargs):
    print("Positional Arguments:")
    for arg in args:
        print(arg)
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

log_args_kwargs(1, 2, 3, name="Rupesh", role="Developer")