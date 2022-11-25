#! /usr/bin/env python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place


"""
provide command line interface to manage
BaseModel object
Inherits cmd class
"""


class HBNBCommand(cmd.Cmd):
    """
    A subclass of cmd that provide command interface

    Methods:
        quit : To exit the program
        help : Provide help about functions
    """

    prompt = '(hbnb) '
    ruler = "="

    def do_quit(self, arg):
        """
        Exits the program
        """
        sys.exit()

    def do_EOF(self, line):
        """
        Ensures control + D quits the program
        """
        return True

    def emptyline(self):
        """
        Empty line doesn't run previous command
        """
        pass

    def do_create(self, name):
        """
        create a new object of class name
        and save it to a json file
        """
        if name:
            if name not in storage.allClass().keys():
                print("** class doesn't exist **")
            else:
                tmp = storage.allClass()[name]()
                tmp.save()
                print(tmp.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        print a string representation of object
        :arg line: class and id
        """
        if line and line != " ":
            args = line.split(" ")
            if args[0] not in storage.allClass().keys():
                print("** class doesn't exist **")
            else:
                if len(args) == 2:
                    keyform = "{}.{}".format(args[0], args[1])
                    if keyform not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        print(storage.all()[keyform])
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")
        storage.save()

    def do_destroy(self, line):
        """
        deletes an objects from a json object
        :arg line: class and id
        """
        if line and line != " ":
            args = line.split(" ")
            if args[0] not in storage.allClass().keys():
                print("** class doesn't exist **")
            else:
                if len(args) == 2:
                    keyform = "{}.{}".format(args[0], args[1])
                    if keyform not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        del storage.all()[keyform]
                        storage.save()
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        print the string representation of the objects in the class
        :param line: specify type of class to print
        :return: void
        """
        tmp = []
        if line:
            if line in storage.allClass().keys():
                tmp = [str(v) for (k, v) in storage.all().items()
                       if v.to_dict()['__class__'] == line]
            else:
                print("** class doesn't exist **")
                return
        else:
            tmp = [str(i) for i in list(storage.all().values())]
        print(tmp)

    def do_update(self, line):
        """
        update an object in base model
        :param line: a string that contain class name id attribute value
        :return:void
        """
        if line and line != "":
            args = line.split(' ')
            # if class is valid
            if args[0] in storage.allClass().keys():
                # if id was not giving
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                else:
                    # get key form from id
                    keyform = "{}.{}".format(args[0], args[1])
                    # check if there is not instance
                    if keyform not in storage.all().keys():
                        print("** no instance found **")
                        return
                    else:
                        # check if  attribute was not giving
                        if len(args) < 3:
                            print("** attribute name missing **")
                            return
                        # check if value was not giving
                        if len(args) < 4:
                            print("** value missing **")
                            return
                        # Get the object to modify
                        # Get a particular attribute to modify using
                        if type(getattr(storage.all()[keyform], args[2])) \
                                is str:
                            setattr(storage.all()[keyform], args[2], args[3])
                        elif type(getattr(storage.all()[keyform], args[2])) \
                                is int:
                            setattr(storage.all()[keyform], args[2],
                                    int(args[3]))
                        elif type(getattr(storage.all()[keyform], args[2]))\
                                is float:
                            setattr(storage.all()[keyform], args[2],
                                    float(args[3]))
                        else:
                            setattr(storage.all()[keyform], args[2],
                                    float(args[3]))

                        storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
