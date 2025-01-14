#!/usr/bin/python3
'''console module'''
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(Cmd):
    '''HBNBCommand class'''
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State',
               'City', 'Place', 'Review', 'Amenity']

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
            my_obj = eval(args)()
            my_obj.save()
            print(my_obj.id)

    def do_show(self, args):
        '''Prints the string representation of an
        instance based on the class name and id'''
        arguments = args.split()
        my_objs = storage.all()

        if len(arguments) == 0:
            print('** class name missing **')
        elif len(arguments) > 0 and arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            my_obj = None
            for obj in my_objs.values():
                if type(obj).__name__ == arguments[0]\
                        and arguments[1] == obj.id:
                    my_obj = obj
            if my_obj:
                print(my_obj)
            else:
                print('** no instance found **')

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
            my_obj = None

            for obj in my_objs.values():
                if type(obj).__name__ == arguments[0]\
                        and arguments[1] == obj.id:
                    my_obj = obj

            if my_obj:
                del my_objs[f'{type(my_obj).__name__}.{my_obj.id}']
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

        elif len(arguments) == 1 and arguments[0] not in self.classes:
            print("** class doesn't exist **")

        else:
            class_based_objs = []
            for obj in my_objs.values():
                if type(obj).__name__ == arguments[0]:
                    class_based_objs.append(obj)

            for obj in class_based_objs:
                print(obj)

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

    def default(self, arg):
        '''retrieve all instances of a class by using: <class name>.all()'''
        sliced_argument = arg.split('.')

        if len(sliced_argument) == 1 \
                and sliced_argument[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(sliced_argument) == 1 and sliced_argument[0] in self.classes:
            return None

        else:
            if sliced_argument[1] == 'all()':
                self.collect(sliced_argument[0])

            elif sliced_argument[1] == 'count()':
                res = self.count(sliced_argument[0])
                print(res)

            elif 'show' in sliced_argument[1]:
                id = sliced_argument[1][5:-1].strip('"')
                if id == '' or id is None:
                    print("** instance id missing **")
                else:
                    my_objs = storage.all()
                    my_obj = None
                    for obj in my_objs.values():
                        if type(obj).__name__ == sliced_argument[0]\
                                            and id == obj.id:
                            my_obj = obj
                    if my_obj:
                        print(my_obj)
                    else:
                        print('** no instance found **')
            else:
                pass

    def collect(self, cls):
        '''collect all objects with specific class'''
        my_objs = storage.all()
        class_based_objs = []
        for obj in my_objs.values():
            if type(obj).__name__ == cls:
                class_based_objs.append(obj)

        for obj in class_based_objs:
            print(obj)

    def count(self, cls):
        '''counts the objects based to class name'''
        my_objs = storage.all()
        class_based_objs = []

        for obj in my_objs.values():
            if type(obj).__name__ == cls:
                class_based_objs.append(obj)

        return len(class_based_objs)

    def show(self, cls):
        '''retrieve an instance based on its ID'''

    def emptyline(self):
        '''empty line + ENTER shouldn't execute anything'''
        print('** class name missing **')
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
