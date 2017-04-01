import re

class ContactInfo():
    """
    Describes properties of a contact
    """
    
    def __init__(self):
        # If we are able to parse out these values, we replace as we go. 
        self.name = "Unable to extract"
        self.number = "Unable to extract"
        self.email = "Unable to extract"
    
    """
    Including these 'getters' as part of the interface specification.
    """
    def getName(self):
        return self.name
    
    def getPhoneNumber(self):
        return self.NormalizePhoneNumber()
    
    def getEmailAddress(self):
        return self.email
    
    def printContactInfo(self):
        """
        Prints the current properties of the contact in the format described by the requirements.
        """
        print("Name: %s" % str(self.name))
        print("Phone: %s" % str(self.getPhoneNumber()))
        print("Email: %s" % str(self.email))
    
    def NormalizePhoneNumber(self):
        """
        strips out any non nummeric charaters from the contact phone number
        """
        return re.sub('[^0-9]','', self.number)
