from business_card_parser import BusinessCardParser
from config import Config
conf = Config()

def main():
    """
    Takes the OCR input from the 'input.txt' file, extracts out the contact information, and displays the result.
    """
    
    # Worker that parses the contact information from the OCR input file.
    parser = BusinessCardParser()
    # Get ocr input
    ocr_input = getOcrInput()
    print("Parsing this ocr input...\n%s" % str(ocr_input))
    print("=================")
    # Parse out Name, email, and phone number
    contact = parser.getContactInfo(ocr_input)
    print("Result")
    print("=================")
    contact.printContactInfo()
    
def getOcrInput():
    """
    Retrieves the input from the OCR output file and returns the file as a string.
    """
    try:
        with open(conf.get_value('INPUT_FILE')) as in_file:
           return in_file.read() 
    except Exception as e:
        print("Error reading input file: %s" % e)

if __name__ == "__main__":
    main()