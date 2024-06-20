import sys
from error import Error
from morse_code import Morse
from caesar_cipher import Caesar


class Main:
    @staticmethod
    def main():

        if len(sys.argv) != 3:
            Error.error_message("Inappropriate amount of command-line arguments. The correct usage is as following:\n"
                                + "python main.py <Path of the input file> <Path of the output file>")

        try:
            i = open(sys.argv[1], "r")
        except PermissionError:
            Error.error_message("Permission denied for the input file.")
        except FileNotFoundError:
            Error.error_message("Input file does not exist.")

        try:
            o = open(sys.argv[2], "w")
        except PermissionError:
            Error.error_message("Permission denied for the output file.")

        input_lines = InputReader([line for line in i])
        i.close()

        for line in input_lines.message:
            print(line, end="")
            o.write(line)
            o.flush()
        o.close()



class InputReader:
    def __init__(self, lines):
        self.crypt = lines[0]
        self.operation = lines[1]
        self.code = lines[2:]
        self.message = []

        match self.operation:
            case "Encode\n":
                self.message = self.encode()
            case "Decode\n":
                self.message = self.decode()

    def encode(self):
        args = self.code, True
        match self.crypt:
            case "Morse\n":
                return Morse.msg(*args)
                # Morse.encode
            case "Caesar\n":
                return Caesar.msg(*args)

    def decode(self):
        args = self.code, False
        match self.crypt:
            case "Morse\n":
                return Morse.msg(*args)
            case "Caesar\n":
                return Caesar.msg(*args)




if __name__ == "__main__":
    Main.main()
