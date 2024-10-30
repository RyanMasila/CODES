#!/usr/bin/python3
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    FRIENDS = [ "Amalia", "Ryan", "Bob", "Ace", "Nadine" ]

    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = 'hello, ' + person
        else:
            greeting = 'hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [
                    f 
                    for f in self.FRIENDS
                    if f.startswith(text)
                    ]
        return completions

    def help_greet(self):
        print('\n'.join([ 'greet [person]',
                            'Greet the named person'
                         ]))

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
