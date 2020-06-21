import sys

class Flags:
    pass

class FlagDefinition:
    def __init__(self,
                 flag_name,
                 short_alias=None,
                 flag_type=None,
                 default_value=None,
                 internal_name=None,
                 description=None):
        self.flag_name = flag_name
        self.short_alias = short_alias
        self.flag_type = flag_type
        self.default_value = default_value
        self.internal_name = internal_name
        self.description = description


class Command:
    def __init__(
        self, 
        use,
        aliases=None,
        suggest_for=None,
        short=None,
        long=None,
        example=None,
        deprecated=None,
        hidden=None,
        run=None,
        args=None
    ):
        self.use = use

        self.aliases = aliases

        self.suggest_for = suggest_for

        self.short = short

        self.long = long

        self.example = example

        self.deprecated = deprecated

        self.hidden = hidden

        self.run = run

        self.args = args

        self.commands = []

        self.parent = None

        self.help_command = None

        self.flag_defs = []

        self.flags = Flags()

    def add_command(self, command):
        if not isinstance(command, Command):
            raise TypeError('Command must be of type command')
        command.parent = self
        self.commands.append(command)

    def persistent_flags(self):
        pass

    def flags(self):
        pass

    def add_flag(self,
                 flag_name,
                 short_alias=None,
                 flag_type=None,
                 default_value=None,
                 internal_name=None,
                 description=None):
        flag = FlagDefinition(flag_name, short_alias, flag_type, default_value, internal_name, description)
        self.flag_defs.append(flag)

    def has_parent(self):
        return parent != None

    def root(self):
        if self.has_parent():
            return self.parent.root()
        return self

    def name(self):
        name = self.use
        i = name.find(' ')
        if i != -1:
            name = name[:i]
        return name

    def help(self):
        pass

    def init_default_help_flag(self):
        pass

    def init_help_cmd(self):
        if len(self.commands) == 0:
            return

        def help_func():
            cmd, _, e = self.root().find()
            if cmd == None or e != None:
                #TODO print args
                print('Unknown help topic ...')
                self.root().usage()
            else:
                self.init_default_help_flag()
                self.help()

        if self.help_command == None:
            self.help_command = Command(
                use='help [command]',
                short='Help about any command',
                long=('Help provides help for any command in the application.\n'
                     'Simply type {self.name()} help [path to command] for full details.'),
                run=lambda: None
            )



    def init_complete_cmd(self):

    def find(self):
        def innerfind():
            pass
        pass

    def execute(self):
        #TODO context.Background()

        if self.has_parent():
            return self.root().execute()

        #TODO preExecHook windows hook

        #self.init_help_cmd()

        if self.args == None:
            self.args = sys.argv[1:]

        #self.init_complete_cmd()

        #TODO TraverseChildren
        cmd, flags, err = self.find()
        
        #TODO error handling

        return cmd, err
