from .flag import Flag


class FlagSet:
    def __init__(self):
        self.usage = lambda x: print(x)
        self.flags = {}
        self.set_flags = {}
        self.shorthands = {}
        self.args = []
        self.parsed = False
        self.args_len_at_dash = -1

    def add_flagset(self, flagset):
        self.flags.update(flagset.flags)

    def add_flag(self, typ, name, value, shorthand=None, usage=None):
        flag = Flag(typ=typ, name=name, value=typ(value), shorthand=shorthand, usage=usage, def_value=str(value))
        if name in self.flags:
            # TODO
            print('PANIC FLAG ALREADY EXISTS')
            return

        # TODO normalize
        self.flags[name] = flag

        if not shorthand:
            return

        # TODO
        if len(shorthand) > 1:
            print('SHORTHAND TOO LONG')
            return

        if shorthand in self.shorthands:
            print('SHORTHAND ALREADY EXISTS')
            return
        self.flags[shorthand] = flag

    def set_flag(self, name, value):
        # TODO normalize
        nname = name

        if nname not in self.flags:
            # TODO
            print(self.flags)
            print(nname)
            print('No such flag')
            return ValueError

        flag = self.flags[nname]

        err = flag.set_value(value)
        if err is not None:
            if flag.shorthand != '':
                flag_name = '-{}, --{}'.format(flag.shorthand, flag.name)
            else:
                flag_name = '--{}'.format(flag.name)
            print('invalid argument {} for {} flag: {}'.format(value, flag_name, err))
            return ValueError

        if not flag.changed:
            self.set_flags[nname] = flag
            flag.changed = True

        if flag.deprecated:
            # TODO
            print('Flag --{} has been deprecated, {}'.format(flag.name, flag.deprecated))
        return None

    def parse(self, args):
        self.parsed = True

        if len(args) <= 0:
            return None

        err = self.parse_args(args)

        if err is not None:
            # TODO error handling
            print("main parse error")
            exit(2)

        return None

    def parse_args(self, args):
        while len(args) > 0:
            s = args[0]
            args = args[1:]

            if len(s) == 0 or s[0] != '-' or len(s) == 1:
                self.args.append(s)
                self.args.extend(args)
                return None

            if s[1] == '-':
                if len(s) == 2:
                    self.args_len_at_dash = len(self.args)
                    self.args.extend(args)
                    break
                args, err = self.parse_long_args(s, args)
            else:
                args, err = self.parse_short_args(s, args)

            if err is not None:
                return err
        return None

    def parse_long_args(self, s, args):
        a = args
        name = s[2:]
        print(a, name)

        if len(name) == 0 or name[0] == '-' or name[0] == '=':
            print('bad flag syntax {}'.format(s))
            return a, ValueError()

        # TODO normalize
        split = name.split('=')
        name = split[0]

        if name not in self.flags:
            #TODO
            return a, ValueError()

        flag = self.flags[name]
        if len(split) == 2:
            value = split[1]
        elif flag.no_opt_def_val:
            value = flag.no_opt_def_val
        elif len(a) > 0:
            value = a[0]
            a = a[1:]
        else:
            print('flag needs an argument: {}'.format(s))
            return a, ValueError()

        err = self.set_flag(flag.name, value)
        if err is not None:
            print('ERROR parse long args')
        return a, err

    def parse_short_args(self, s, args):
        shorthands = s[1:]

        while len(shorthands) > 0:
            shorthands, a, err = self.parse_single_short_arg(shorthands, args)
            if err is not None:
                return a, err
        return a, err

    def parse_single_short_arg(self, shorthands, args):
        out_args = args

        out_shorts = shorthands[1:]
        c = shorthands[0]

        if c not in self.shorthands:
            # TODO
            return out_shorts, out_args, ValueError()

        flag = self.shorthands[c]

        if len(shorthands) > 2 and shorthands[1] == '=':
            value = shorthands[2:]
            out_shorts = ''
        elif flag.no_opt_def_val != '':
            value = flag.no_opt_def_val
        elif len(shorthands) > 1:
            value = shorthands[1:]
            out_shorts = ''
        elif len(args) > 0:
            value = args[0]
            out_args = args[1:]
        else:
            print("ERROR parse short arg")
            # TODO
            return out_shorts, out_args, ValueError()

        # TODO shorthand_deprecated

        err = self.set_flag(flag.name, value)
        if err is not None:
            print("ERROR parse short arg 2")
        return out_shorts, out_args, err
