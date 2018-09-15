#!/usr/bin/env python

import argparse
from .contact import Contact
import yaml
import os
from .validations import validate_phone_number, validate_email


class PyContacts:
    """
    Tool to store contacts in yaml
    """

    def __init__(self):
        self.contact = Contact()
        self.file_name = 'py_contacts.yaml'
        self.contacts_found = []

    def parse_input(self, input_args):
        """
        Received parameter is converted into Contact object by assigning the
        values to respective class attributes.
        :param input_args: command line arguments
        """
        for k, v in input_args.__dict__.items():
            if hasattr(self.contact, k):
                setattr(self.contact, k, v)

    def add_contact(self):
        """
        Appends the contact to the yaml file.
        """
        contact_to_store = dict()
        if not self.contact.name or not self.contact.number:
            raise argparse.ArgumentTypeError("Contact name and contact number is needed to create a contact")
        contact_to_store[(self.contact.name, self.contact.number)] = self.contact.get_contact()
        with open(self.file_name, 'a+') as outfile:
            yaml.dump(contact_to_store, outfile, default_flow_style=False, allow_unicode=True)
        print ("Contact creation successful")

    def list_contacts(self):
        """
        Lists all contacts in the yaml file.
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as stream:
                data = yaml.load(stream)
            self.__print_contact(data)

    def show_contact(self):
        """
        Finds the contact based on the command line arguments.
        """
        if not self.contact.name:
            raise argparse.ArgumentTypeError("Specify the contact name to search")

        with open(self.file_name, 'r') as stream:
            data = yaml.load(stream)

        for k, v in data.items():
            if k[0] == self.contact.name:
                if self.contact.number and k[1] == self.contact.number:
                    self.contacts_found = []
                    self.contacts_found.append(v)
                    break
                else:
                    self.contacts_found.append(v)

        if not self.contacts_found:
            raise Exception("Contact not found")
        self.__print_contact()

    def __print_contact(self, contacts=None):
        """
        Utility function to print output to the terminal
        """
        if contacts:
            for k, v in contacts.items():
                for ik, iv in v.items():
                    print ("%s: %s" % (ik, iv))
                print ("\n")
        else:
            for contact in self.contacts_found:
                for k, v in contact.items():
                    print ("%s: %s" % (k, v))
                print ("\n")

    def remove_contact(self):
        """
        Deletes a contact from the yaml file.
        """
        if not self.contact.name or not self.contact.number:
            raise argparse.ArgumentTypeError("Contact name and contact number is needed to remove a contact")

        with open(self.file_name, 'r') as stream:
            data = yaml.load(stream)

        for k, v in data.items():
            if k[0] == self.contact.name and k[1] == self.contact.number:
                del data[k]
                break

        with open(self.file_name, 'w+') as outfile:
            yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

        print ("Contact deletion successful")

    def process_input(self, arguments):
        """
        Delegates the control to the respective function based on the input arguments.
        :param arguments: command line arguments
        """
        self.parse_input(arguments)
        try:
            if arguments.add:
                self.add_contact()
            elif arguments.list:
                self.list_contacts()
            elif arguments.show:
                self.show_contact()
            elif arguments.remove:
                self.remove_contact()
            else:
                print ("Invalid operation")
        except Exception as e:
            print (str(e))


def main():
    try:
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--add',
                            help='Add a contact', action="store_true")
        parser.add_argument('--list',
                            help='List all contact', action="store_true")
        parser.add_argument('--show',
                            help='Show respective contact', action="store_true")
        parser.add_argument('--remove',
                            help='Remove respective contact', action="store_true")
        parser.add_argument('--name', type=str, help="contact name", required=False)
        parser.add_argument('--number', type=validate_phone_number, help="contact number", required=False)
        parser.add_argument('--email', type=validate_email, default=None, help="email id of the contact", required=False)
        parser.add_argument('--address', type=str, default=None, help="address of the contact", required=False)
        parser.add_argument('--notes', type=str, default=None, help="notes", required=False)
        args = parser.parse_args()
        obj = PyContacts()
        obj.process_input(args)
    except argparse.ArgumentTypeError as e:
        print (e)

