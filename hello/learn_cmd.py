#!/usr/bin/python3
import cmd
"""visit to discover more about cmd module 
https://cloudmesh.github.io/classes/lesson/prg/python_cmd.html"""


class Calculator(cmd.Cmd):
    prompt = 'calculator >>> '
    intro = 'Simple calculator that can do addition, subtraction, multiplication and division.'

    def do_add(self, line):
        args = line.split()
        total = 0
        for arg in args:
            total += float(arg.strip())
        print(total)

    def do_subtract(self, line):
        args = line.split()
        total = 0
        if len(args) > 0:
            total = float(args[0])
        for arg in args[1:]:
            total -= float(arg.strip())
        print(total)

    def help_add(self):
        print('\n'.join([
        'add [number,]',
        'Add the arguments together and display the total.'
        ]))

    def help_subtract(self):
        print('\n'.join([
        'subtract [number]',
        'Subtract all following arguments from the first argument.'
        ]))

    def do_EOF(self, line):
        print('bye, bye')
        return True


if __name__ == '__main__':
     Calculator().cmdloop()




'''class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, person):
        if person:
            print("hi,", person)
        else:
            print('hi')

    def help_greet(self):
        print('\n'.join([ 'greet [person]',
                           'Greet the named person',
                           ]))

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
'''


'''class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print('hi')

    def do_EOF(self, line):
        return True
    
    def do_postloop(self, line):
        print()

if __name__ == '__main__':
    HelloWorld().cmdloop()
'''



"""class HelloWorld(Cmd):
    'Simple command processor example'

    def do_greet(self, line):
        print("hello")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
"""

