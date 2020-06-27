import cobry

def add_int(args):
    _sum = 0
    for i, val in enumerate(args):
        try:
            val = int(val)
        except:
            print('ERROR: argument {} is not an integer: given {}'.format(i, val))
            return
        _sum = _sum + val
    print('Sum of {} is {}'.format(args, _sum))


add_cmd = cobry.Command(
    use='add',
    short_desc='A brief description of your command',
    long_desc='''A longer description that spans multiple lines and likely contains 
examples and usage of using your command. For example:

Cobry is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobry application.''',
    run=add_int
)
