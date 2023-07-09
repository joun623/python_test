def a(x):
    y = 100
    def b():
        z = 10000
        def c():
            print(z)
            print(y)
            print(x)
            print(free_val)

        c()
    b()

def outer():
    x = "outer"

    def inner():
        print(x)

    def dynamic():
        x = "dynamic"
        inner()
    dynamic()

outer()
