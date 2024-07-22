def convert_type(data_type):
    def convert_type_decorator(func):
        def wrapper():
            return data_type(func())
        return wrapper
    return convert_type_decorator