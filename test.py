# def my_decorator(func):
#     def wrapper():
#         print('wrapper of decorator')
#         func()
#     return wrapper
#
# def greet():
#     print('hello world')
#
# greet = my_decorator(greet)
# greet()
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper
@my_decorator
def greet():
    print('hello world')

greet()
