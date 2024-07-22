def generate_multiples(number):
    def make_multiples(amount):
        numbers = []
        for i in range(0, amount):
            numbers.append(number * (i+1))
        return numbers
    return make_multiples


def capitaliser(func):
    if isinstance(func(), str):
        def convert_to_upper_case():
            return func().upper()
        return convert_to_upper_case
    return func



# Advanced Challenge - Come back later!
def secure_func():
    # implement me
    pass
