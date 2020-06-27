import cobry
from .add import add_cmd


def run(args):
    print('Hello CLI')
    if len(args) > 0:
        print('You have given me the following commands: {}'.format(args))


root_cmd = cobry.Command(
    use='my-calc',
    short_desc='A brief description of your application',
    long_desc='''A longer description that spans multiple lines and likely contains 
examples and usage of using your application. For example:
    
Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.''',
    run=run
)


def init_config():
    pass


def init():
    root_cmd.on_initialize(init_config)
    root_cmd.add_command(add_cmd)


def execute():
    init()
    err = root_cmd.execute()
    if err is not None:
        print(err)
        exit(1)
