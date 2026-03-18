# create a one function there inside create two decorators 1 is only allow numbers, 2 is only allow characters and then call the function with both decorators
def only_numbers(func):
    def execute(a):
        if str(a).isdigit():
            return func(a)
        else:
            print("invalid data")
    return execute

# def only_characters(func):
#     def execute(a):
#         if str(a).isalpha():
#             return func(a)
#         else:
#             print("invalid data")
#     return execute

