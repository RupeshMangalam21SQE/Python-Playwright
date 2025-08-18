class MyContext:
    def __enter__(self):
        print("Entering Context")
        return self  # optional, can return something
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")

# Using custom context manager
with MyContext():
    print("Inside the context")
