import json
import re
from contact_info import ContactInfo

class BusinessCardParser:
    """
    Handles the parsing of the OCR business card output.
    """
    
    def __init__(self):
        # This object is used to store the resulting contact information.
        self.contact = ContactInfo()
    
    def getContactInfo(self, document_string):
        """
        Parses the output of a business card string and returns a ContactInfo object.
        inputs: document_string, the string extracted from the business card OCR reading.
        returns: ContactInfo, an object representing the contact information extracted from the document_string.
        """
        input_lines = document_string.split('\n')
        
        # Step 1 : Identify Phone number
        phone_index = self._determinePhoneNumberIndex(input_lines)
        if phone_index != -1:
            self.contact.number = input_lines[phone_index]
            # Remove phone number from input_lines because it was already processed.
            del input_lines[phone_index]
        
        # Step 2: Identify Email
        email_index = self._determineEmailIndex(input_lines)
        if email_index != -1:
            self.contact.email = input_lines[email_index]
            # Remove email from input_lines because it was already processed.
            del input_lines[email_index]
        
        # Step 3: Identify Name
        name_index = self._determineNameIndex(input_lines)
        if name_index != -1:
            self.contact.name = input_lines[name_index]
            # Remove name from input_lines because it was already processed.
            del input_lines[name_index]
        
        return self.contact
    
    def _determinePhoneNumberIndex(self,input_lines):
        """
        Given a list of strings, will return the index of the phone number. -1 if not found.
        input: list of strings retrieved from the ocr input.
        returns: integer representing the index of the phone number. -1 if not found.
        """
        index = -1
        for i,line in enumerate(input_lines):
            line = line.lower().strip() # Clean up any whitespace and normalize to lower case
            # If number of digits in string >= 10, and not fax number
            if self._countNumDigits(line) >= 10 and not any(faxWord in line for faxWord in ['fax', 'fx']):
                return i
        return index
    
    def _determineEmailIndex(self,input_lines):
        """
        Given a list of strings, will return the index of the email address. -1 if not found.
        input: list of strings retrieved from the ocr input.
        returns: integer representing the index of the email address. -1 if not found.
        """
        index = -1
        for i,line in enumerate(input_lines):
            line = line.strip() # Clean up any whitespace
            
            # regex looks for the format email@something.suffix,
            # Allows for one '@', and at least one '.' after the '@'
            email_format = re.compile("[^@]+@[^@]+\.[^@]+")
            if len(line.split()) == 1 and email_format.match(line):
                return i
        return index
    
    def _determineNameIndex(self, input_lines):
        """
        Given a list of strings, will return the index of the name. -1 if not found.
        input: list of strings retrieved from the ocr input.
        returns: integer representing the index of the name. -1 if not found.
        """
        index = -1
        possible_names = [] # list storing candidates for names. {index, name}
        for i,line in enumerate(input_lines):
            line = line.strip() # Clean up any whitespace
            
            # Looking for format 'Word Word'  (No consecutive upper case chars)
            name_format = re.compile("[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+")

            # If no digits, special characters, and 2 words, add to possible candidates
            if self._countNumDigits(line) == 0 and len(line.split())== 2 and len(name_format.findall(line)) == 1:
                possible_names.append({'index': i,'name': line})
        
        # For potential names, check if 1st word is in list of common names
        names_db = []
        with open('names.dat', 'r') as names_file:
            lines = names_file.readlines()
            # remove whitespace
            for line in lines:
                names_db.append(line.replace('\n',''))
                
        for name in possible_names:
            f_name = name['name'].split()[0]
            if f_name in names_db:
                return name['index']
        return index
        
    
    def _countNumDigits(self,input):
        """
        Given a string, count the number of digits
        input: a string
        returns: number of digits in the string
        """
        num_digits = 0
        for char in input:
            if char.isdigit():
                num_digits += 1
        return num_digits
                
