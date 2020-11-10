# Importing packages
import os
from base64 import b64encode, b64decode

# Creating a class to make decoder and encoder
class encodeDecode:

    def __init__(self):
        
        pass

    # encode method
    def encode(self, msg):

        self.msg = msg

        return b64encode(self.msg)

    # decode method
    def decode(self, msg):

        self.msg = msg
        
        return b64decode(self.msg)

# Creating an object of class 'encodeDecode' 
obj = encodeDecode()

# Encode function with wrapper
def encode():

    text = str(input("[In] Enter the text to encode: ")).encode()

    print(f"[Info] You Entered: {str(text)}\n")
    print('')
    print(f"[Out] Encoded text: {str(obj.encode(text))}\n")

# Decode function with wrapper
def decode():
    
    try:
        text = str(input("[In] Enter the encoded-text to decode: "))
        print('')
        print(f"[Info] You Entered: {str(text)}\n")
        print(f"[Out] Decoded text: {obj.decode(text)}\n")
    
    except Exception as err:

        print("Please enter correct encoded text!")
        print(err)

# Program Banner
def banner():

    os.system('clear')

    text = """
    \033[1;31;40m
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Welcome to Enco-Deco!\n
    Here you can encode and decode text and do many awesome stuff!\n
    *********************************\n
    *  |\  | |****| ***** |****     *\n
    *  | \ | |    |   |   |----     *\n
    *  |  \| |____|   |   |____     *\n
    *********************************
    *This is just a wrapper for people who don't know about programming\n    and this will help those to encode
    text. Enjoy encoding!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n
    """

    print(text)
    action()

# Commands in program
def action():

    text="""
    \033[1;32;40m
    **************************************\n
    * What you want to do now?           *\n
    *  1. Encode Text |Base64|           *\n
    *  2. Decode encoded text |Base64|   *\n
    *  3. Banner                         *\n
    *  4. Quit Program                   *\n
    *  5. About Us                       *\n
    **************************************\n

    """
    print(text)

# About me
def aboutUs():
    
    text = """
    About Me:
    Hello, world! I am Muhammed Rajab. I am very interested in AI, Data Science and Computer Vision.\n
    This is my first project in Python. I know it is pretty simple program.\n
    I Just Wanted to make some projects that is fun.\n
    For business queries:
    
    e-mail: muhammedrajab1324@gmail.com

    """
    
    print(text)

banner()

# Create an infinite loop and continues till user exits...
while True: 


    print("\n"*2)

    cmd = str(input("\033[1;34;40m[+] Enter Command [1 to 5]>$ "))
    print('')

    if cmd == '1':
        
        encode()

    elif cmd == '2':
        
        decode()

    elif cmd == '3':

        banner()
        action()
    
    elif cmd == '4':

        confirm = str(input("[+] Do you want to Exit [Y/N]>$ "))

        if confirm.lower() == 'y':
            print("\nThank you for using my code!\n")
            print("[-] Exiting Program....")
            exit()

        else:

            continue

    elif cmd == '5':

        aboutUs()

    else:
        os.system('clear')
        print("Wrong Command: ", cmd)
        continue
