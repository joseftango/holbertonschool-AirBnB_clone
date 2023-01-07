#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
"""importing modules"""


class HBNBCommand(cmd.Cmd):
    '''class named HBNBCommand'''
    prompt = '(hbnb) '
    my_classes = ['BaseModel', 'City', 'Place', 'Review',
    'State', 'User', 'Amenity']

    def do_quit(self, arg):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program\n'''
        return True

    def only_enter(self, arg):
        '''empty line + enter should not execute anything\n'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id'''
        val_arg = arg.split(' ')

        if len(val_arg[0]) == 0:
            print('** class name missing **')
            return

        elif len(val_arg[0]) > 0 and val_arg[0] not in self.my_classes:
            print("** class doesn't exist **")
            return

        elif val_arg[0] in self.my_classes:
            new_obj = eval(val_arg[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        '''Prints the string representation of an
        instance based on the class name and id'''
        val_arg = arg.split(' ')

        if len(val_arg[0]) == 0:
            print("** class name missing **")
            return

        elif len(val_arg) >= 1 and val_arg[0] not in self.my_classes:
            print("** class doesn't exist **")
            return

        elif len(val_arg) == 1 and val_arg[0] in self.my_classes:
            print('** instance id missing **')
            return

        elif len(val_arg) == 2:
            storage.reload()
            my_data = storage.all()

            if my_data.get(f'{val_arg[0]}.{val_arg[1]}'):
                print(my_data[f'{val_arg[0]}.{val_arg[1]}'])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        val_arg = arg.split(' ')

        if len(val_arg[0]) == 0:
            print("** class name missing **")
            return

        elif len(val_arg) >= 1 and val_arg[0] not in self.my_classes:
            print("** class doesn't exist **")
            return

        elif len(val_arg) == 1 and val_arg[0] in self.my_classes:
            print('** instance id missing **')
            return

        elif len(val_arg) == 2:
            storage.reload()
            my_data = storage.all()

            if my_data.get(f'{val_arg[0]}.{val_arg[1]}'):
                del my_data[f'{val_arg[0]}.{val_arg[1]}']
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        val_arg = arg.split(' ')
        my_list = []
        storage.reload()
        my_obj = storage.all()

        if len(val_arg) == 1:
            if val_arg[0] not in self.my_classes:
                print("** class doesn't exist **")
                return
            for k, v in my_obj.items():
                my_list.append(v)

        else:
            for k, v in my_obj.items():
                my_list.append(v)
        print(my_list)

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        val_arg = args.split()
        if not val_arg:
            print("** class name missing **")
            return
        if val_arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            val_arg[1]
        except Exception:
            print("** instance id missing **")
            return
        storage.reload()
        objects_dict = storage.all()
        my_key = val_arg[0] + "." + val_arg[1]
        if my_key not in objects_dict:
            print("** no instance found **")
            return
        try:
            val_arg[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            val_arg[3]
        except Exception:
            print("** value missing **")
            return
        if val_arg[3]:
            my_dict = objects_dict[my_key]
            setattr(my_dict, val_arg[2], val_arg[3])
            setattr(my_dict, 'updated_at', datetime.now())
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
