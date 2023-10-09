#!/usr/bin/python3
""" module contains console for command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Initializing infinite loop and prompt to display """
    prompt = '(hbnb) '
    class_list = [
        "BaseModel",
        # "Amenity",
        # "City",
        # "Place",
        # "Review",
        # "State",
        # "User"
    ]

    def emptyline(self):
        """If line is empty, do nothing"""
        pass

    def do_EOF(self, *line):
        """Quits upon receiving EOF as input"""
        print()
        return True

    def do_quit(self, *line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves to JSON"""
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if class_name not in self.class_list:
                print('** class doesn\'t exist **')
                return
            else:
                object = eval(class_name)()
                object.save()
                print(object.id)

    def do_show(self, line):
        """Prints string representation of instance based on class name"""
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        else:
            class_name = line.split()[0]
            if class_name not in self.class_list:
                print('** class doesn\'t exist **')
                return
            elif len(args) < 2:
                print('** instance id missing **')
                return
            else:
                obj_id = args[1]
                obj_dict = storage.all()
                obj_key = f'{class_name}.{obj_id}'
                if obj_key not in obj_dict:
                    print('** no instance found **')
                    return
                print(obj_dict[obj_key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if class_name not in self.class_list:
                print('** class doesn\'t exist **')
                return
            elif len(args) < 2:
                print('** instance id missing **')
                return
            else:
                obj_id = args[1]
                obj_dict = storage.all()
                obj_key = f'{class_name}.{obj_id}'
                if obj_key not in obj_dict:
                    print('** no instance found **')
                    return
                del obj_dict[obj_key]
                storage.save()

    def do_all(self, line):
        """Prints string representation of all instances based on class"""
        args = line.split()
        if args:
            class_name = args[0]
            if class_name not in self.class_list:
                print('** class doesn\'t exist **')
                return
            else:
                obj_dict = storage.all()
                obj_list = []
                for key, value in obj_dict.items():
                    if key.split(".")[0] == class_name:
                        obj_list.append(value)
        else:
            obj_list = storage.all().values()
        for obj in obj_list:
            print(str(obj))

    def do_update(self, line):
        """Updates an instance based class name, id by adding an attribute"""
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if class_name not in self.class_list:
                print('** class doesn\'t exist **')
                return
            elif len(args) == 1:
                print('** instance id missing **')
                return
            else:
                obj_id = args[1]
                obj_dict = storage.all()
                obj_key = f'{class_name}.{obj_id}'
                obj = obj_dict.get(obj_key)
                if not obj:
                    print('** no instance found **')
                    return
                elif len(args) == 2:
                    print('** attribute name missing **')
                    return
                elif len(args) == 3:
                    print('** value missing **')
                    return
                else:
                    attribute = args[2]
                    attr_value = args[3]
                    setattr(obj, attribute, attr_value.replace('"', ''))
                    obj.save()

    def do_clear(self, *line):
        """Clears console display"""
        print("\033[3J\033[H\033[2J")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
