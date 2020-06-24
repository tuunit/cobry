def args_minus_first(arguments, arg):
    if arg in arguments:
        i = arguments.index(arg)
        return arguments[:i] + arguments[i+1:]
    return arguments
