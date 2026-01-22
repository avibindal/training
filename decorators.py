def double(oldfunction):
    def newfunction():
        oldfunction()
        oldfunction()
    return newfunction

@double
def wish():
    print("hello")
wish()

@double
def greet():
    print("hi")
greet()