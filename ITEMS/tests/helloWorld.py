#!/usr/bin/python3
import cmd
class HelloWorld(cmd.Cmd):
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("Hi, ", person)
        else:
            print("Hi")
    def help_greet(self):
        print('\n'.join([ 'greet [person]', 'Greet the named person',]))
    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
