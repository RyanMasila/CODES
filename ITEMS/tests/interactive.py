#!/usr/bin/python3
import cmd

class InteractiveOrCommandLine(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or the command line"""
    def do_greet(self, line):
        print("Hello,", line)

    def do_EOF(self, line):
        return True
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()