def concat_strings(*args):
    return_string = ""
    for arg in args:
        return_string = return_string + str(arg).lower()
    return return_string[::-1]
