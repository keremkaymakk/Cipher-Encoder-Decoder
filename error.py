import sys


class Error:
    @staticmethod
    def error_message(message):
        print("ERROR:",message)
        print("Exiting...")
        sys.exit(-1)
