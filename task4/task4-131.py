morse_code_dict = {'A':'.-'   , 'B':'-...' , 'C':'-.-.' , 'D':'-..'  , 'E':'.'    , 'F':'..-.' , 'G':'--.'  , 
                   'H':'....' , 'I':'..'   , 'J':'.---' , 'K':'-.-'  , 'L':'.-..' , 'M':'--'   , 'N':'-.'   , 
                   'O':'---'  , 'P':'.--.' , 'Q':'--.-' , 'R':'.-.'  , 'S':'...'  , 'T':'-'    , 'U':'..-'  , 
                   'V':'...-' , 'W':'.--'  , 'X':'-..-' , 'Y':'-.--' , 'Z':'--..' , '0':'-----', '1':'.----', 
                   '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', 
                   '9':'----.'}
 
def create_morse_message(text):
    morse_str = ""
    for c in text:
        if c.isalnum():
            morse_str += morse_code_dict[c.upper()]
        morse_str += " "
    return morse_str
 
def main():
    text = input()
    morse = create_morse_message(text.upper())
    print(morse)
 
if __name__ == '__main__':
    main()



