#!/usr/bin/python3

import cmd
import os

class ShellEnabled(cmd.Cmd):

    last_output = ''

    def do_shell(self, line):
        "Run a shell command"
        print("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_echo(self, line):
        "Print the input, replacing '$out' with the output of the last shell command"
        # Obviously not robust
        print (line.replace('$out', self.last_output))

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    ShellEnabled().cmdloop()
