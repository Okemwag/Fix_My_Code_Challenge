#!/usr/bin/python3
""" User class """


class User():
    """ Documentation Of the Class"""

    def __init__(self, email):
        """ this is the init method """
        if type(email) is not str:
            raise TypeError("email must be a string")
        else:
            self.__email = email

    @property
    def email(self):
        """ this is getter for email """
        return self.__email


if __name__ == "__main__":

    u = User("me@gmail.com")
    print(u.email)
