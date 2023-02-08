# SCOPES IN PYTHON
# Local Scope
# Enclosing scope
# Global Scope
# Built-in Scope
my_global = 10


def fn1():
    # enclosing scope: referes to a function inside a function AKA Nested Function
    enclosed_v = 8

    def fn2():
        local_v = 5
        print("Access to Global : ", my_global)
        print("Access to Enclosed : ", enclosed_v)
    fn2()


fn1()
# Built-in Scope: print(), def()
