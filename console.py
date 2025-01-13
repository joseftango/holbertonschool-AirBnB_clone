#!/usr/bin/python3
'''console module'''
from cmd import Cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(Cmd):
    '''HBNBCommand class'''
    prompt = '(hbnb) '
    classes = ['BaseModel']

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        return True

    def do_create(self, args):
        '''Creates a new instance of BaseModel
        then saves it to JSON file'''
        if not args:
            print('** class name missing **')
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, args):
        '''Prints the string representation of an
        instance based on the class name and id'''
        arguments = args.split()
        if len(arguments) == 0:
            print('** class name missing **')
        elif len(arguments) == 1 and arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) == 2:
            my_objs = storage.all()
            obj = None
            for v in my_objs.values():
                if arguments[1] == v.id:
                    obj = v
            if obj:
                print(obj)
            else:
                print('** no instance found **')
        else:
            pass

    def do_destroy(self, args):
        '''Deletes an instance based on the class name
        and id (save change into the JSON file)'''
        arguments = args.split()
        if len(arguments) == 0:
            print('** class name missing **')
        elif len(arguments) > 0 and arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print('** instance id missing **')
        else:
            my_objs = storage.all()
            obj = None
            for v in my_objs.values():
                if arguments[1] == v.id:
                    obj = v
            if obj:
                del my_objs[f'{type(obj).__name__}.{obj.id}']
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''Prints all string representation of all
        instances based or not on the class name'''
        arguments = args.split()
        my_objs = storage.all()

        if len(arguments) == 0:
            for obj in my_objs.values():
                print(obj)

        elif len(arguments) == 1 and arguments[0] in self.classes:
            class_based_objs = []

            for obj in my_objs.values():
                if type(obj).__name__ == arguments[0]:
                    class_based_objs.append(obj)

            for obj in class_based_objs:
                print(obj)

        else:
            pass

    def do_update(self, args):
        '''Updates an instance based on the class name
        and id by adding or updating attribute'''
        arguments = args.split()

        if len(arguments) == 0:
            print('** class name missing **')

        elif len(arguments) > 0 and arguments[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(arguments) == 1:
            print("** instance id missing **")

        elif len(arguments) == 2:
            print('** attribute name missing **')

        elif len(arguments) == 3:
            print('** value missing **')

        else:
            my_objs = storage.all()
            my_key = f'{arguments[0]}.{arguments[1]}'
            my_obj = my_objs.get(my_key)
            if my_obj:
                attribute = arguments[2]
                value = arguments[3].strip('"')
                try:
                    value = eval(value)
                except Exception:
                    pass
                setattr(my_obj, attribute, value)
                storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        '''empty line + ENTER shouldn't execute anything'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
