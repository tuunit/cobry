import cobry

echoTimes = 0

def printFunc(cmd, args):
    print('Print: ' + ','.join(args))

def echoFunc(cmd, args):
    print('Echo: ' + ','.join(args))

def timesFunc(cmd, args):
    for i in range(cmd.flags.echoTimes):
        echoFunc(cmd, args)

printCmd = cobry.Command(
                use='print [string to print]',
                short='Print anything to the screen',
                long=('print is for printing anything back to the screen.\n'
                      'For many years people have printed back to the screen.'),
                run=printFunc)

echoCmd = cobry.Command(
                use='echo [string to echo]',
                short='Echo anything to the screen',
                long=('echo is for echoing anything back.\n'
                      'Echo works a lot like print, except it has child command.'),
                run=echoFunc)

timesCmd = cobry.Command(
                use='times [string to echo]',
                short='Echo anything to the screen more times',
                long=('echo things multiples times back to the user by providing a count and a string.'),
                run=timesFunc)

timesCmd.add_flag(
    flag_name='times',
    short_alias='t',
    flag_type=int,
    default_value=1, 
    internal_name='echoTimes',
    description='times to echo the input')

rootCmd = cobry.Command(use='app')
rootCmd.add_command(printCmd)
rootCmd.add_command(echoCmd)
echoCmd.add_command(timesCmd)

print(rootCmd.use)
print(rootCmd.commands[0].use)
print(rootCmd.commands[1].use)
print(rootCmd.commands[1].commands[0].use)
print(rootCmd.commands[1].commands[0].flag_defs[0].internal_name)
rootCmd.execute()
