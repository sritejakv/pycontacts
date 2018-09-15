# pycontacts
Python command line tool to store contacts using yaml

### Getting Started

A contact is identified uniquely with the combination of (name, number).  A phone number can be associated to only one person. But a person may have more than one phone number.

Ex: The following contacts are identified as unique by the tool - 

1) Joseph, 1234567891
2) Joseph, 9876543213
3) Joseph, 6474638273

### Prerequisites

yaml and argparse python libraries are required for the tool to run

### Installing

By default the yaml file will be created in the folder the commands are run. To change the location of the yaml file, edit the class variable self.file_name in pycontacts.py and give a file name with path of your choice before running setup.py

To install the tool, run the following command:

```
python setup.py install
```

### Usage

A contact has following attributes - name, number, address(optional), notes(optional) and email(optional).

Contact can be created using the following command,

```
pycontacts --add --name hello --number 7658473647
```
```
pycontacts --add --name hello --number 1324356457
```

Updation of address, notes and email is possible as of now. To update any of these fields create a new contact with the name and number similar to the old contact.

```
pycontacts --add --name hello --number 7658473647 --email hello@world.com
```

Listing all the contacts.

```
pycontacts --list
```

Searching a contact.
The following command lists all the contacts with the specified name if found,

```
pycontacts --show --name hello
```
The following command lists the unique contact with the specified name and number if found,

```
pycontacts --show --name hello --number 1324356457
```

To remove a contact, both name and number should be specified.

```
pycontacts --remove --name hello --number 7658473647
```
### Authors

* **Sriteja Kummita**
