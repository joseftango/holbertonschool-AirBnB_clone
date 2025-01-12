#!/usr/bin/python3
'''console module'''
from cmd import Cmd


class HBNBCommand(Cmd):
    '''HBNBCommand class'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        print('', end='')
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        print('', end='')
        return True

    def emptyline(self):
        """empty line + ENTER shouldn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
