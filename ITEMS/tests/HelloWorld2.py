#!/usr/bin/python3
import cmd

class HelloWorld(cmd.Cmd):
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    def do_greet(self, person):
        """Greet the person"""
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = "hello"
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f
                           for f in self.FRIENDS
                           if f.startswith(text)
                           ]
            return completions
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
