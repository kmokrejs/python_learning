from address import Address

class Person:
    
    def __init__(self, first, last, dob, phone, address):
        self.first_mame = first
        self.last_name = last
        self.birth_date = dob
        self.phone_number = phone
        self.addresees = []

        if isinstance(address,Address):
            self.addresees.append(address)
        elif isinstance(address,list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise TypeError("Invalid Address..",)

            self.addresees = address
        else: 
            raise TypeError("Invalid Address...")

        def add_address(self, address):
            if not isinstance(address, Address):
                raise TypeError("Invalid Address...")

            self.addresses.append(address)