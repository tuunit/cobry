def args_minus_first(arguments, arg):
    if arg in arguments:
        i = arguments.index(arg)
        return arguments[:i] + arguments[i+1:]
    return arguments


def strip_flags(args, cmd):
    if len(args) == 0:
        return args

    cmd.merge_persistent_flags()

    commands = []
    #flags = cmd.flags

    while len(args) > 0:
        s = args[0]
        print(s)
        args = args[1:]

        if s == '--':
            break
        elif (s[:2] == '--' and '=' not in s) or (s[:1] == '-' and '=' not in s and len(s) == 2):
            if len(args) <= 1:
                break
            else:
                args = args[1:]
                continue
        elif s != '' and s[:1] != '-':
            commands.append(s)

    print(commands)
    return commands
