import sys
from .args import args_minus_first

class Command:
    def __init__(
            self,
            use,
            short_desc=None,
            long_desc=None,
            run=None):
        self.use = use
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.run = run
        self.args = None
        self.on_init_func = None
        self.commands = []
        self.parent = None

    def execute(self):
        if self.has_parent():
            return self.parent.execute()

        self.on_init_func()

        args = self.args

        if self.args is None:
            args = sys.argv[1:]

        cmd, flags, err = self.find(args)

        if cmd is not None:
            cmd.execute_cmd(flags)
        else:
            print('ERROR command does not exist')

    def execute_cmd(self, args):
        self.run(args)

    def has_parent(self):
        return self.parent is not None

    def find_next(self, next_cmd):
        for cmd in self.commands:
            if cmd.name() == next_cmd:
                return cmd

    def find(self, args):
        def inner_find(c, inner_args):
            args_wo_flags = inner_args
            if len(args_wo_flags) == 0:
                return c, inner_args

            next_cmd = args_wo_flags[0]

            cmd = c.find_next(next_cmd)
            if cmd is not None:
                return inner_find(cmd, args_minus_first(inner_args, next_cmd))
            return c, inner_args

        command_found, a = inner_find(self, args)

        return command_found, a, None

    def name(self):
        name = self.use
        i = name.find(' ')
        if i != -1:
            name = name[:i]
        return name

    def on_initialize(self, func):
        self.on_init_func = func

    def add_command(self, cmd):
        cmd.parent = self
        self.commands.append(cmd)
