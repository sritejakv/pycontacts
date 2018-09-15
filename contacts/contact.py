class Contact:
    """
    Contact class with necessary attributes.
    """

    def __init__(self):
        self._name = None
        self._number = None
        self._notes = None
        self._address = None
        self._email = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nm):
        self._name = nm

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, num):
        self._number = num

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, note):
        self._notes = note

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, add):
        self._address = add

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, eml):
        self._email = eml

    def get_contact(self):
        return {'name': self.name,
                'number': self.number,
                'email': self.email,
                'address': self.address,
                'notes': self.notes
                }
