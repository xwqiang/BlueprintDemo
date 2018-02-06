from functools import wraps



def named(name):
    def tt(some_function):
        def wrapper(*args, **kwargs):
            print("before tt",name)
            new_fun = some_function(*args, **kwargs)
            print("after tt",name)
            return new_fun
        return wrapper
    return tt


def tt(some_function):
    def wrapper(*args, **kwargs):
        print("before wrapper")
        new_fun = some_function(*args, **kwargs)
        print("after wrapper")
        return new_fun
    return wrapper



# @named("lalal")
def my():
    print("my")
#
# def parent():
#     print( "Printing from the parent() function.")
#
#
#     def first_child() :
#         return "Printing from the first_child() function."
#
#
#     def second_child():
#         return "Printing from the second_child() function."
#
#
#     print( first_child())
#     print(second_child())



# just_some_function = tt(parent)
# just_some_function
if __name__=='__main__':
    # my()
    named("lalala")(tt(my))()
    # just_some_function = tt(my)
    # just_some_function()
