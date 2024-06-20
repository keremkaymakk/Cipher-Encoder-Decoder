class Morse:
    morse_characters = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": "/", ".": ".-.-.-",
        ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "-": "-....-",
        "(": "-.--.", ")": "-.--.-", '"': ".-..-.", ":": "---...", "=": "-...-", "{": "-.--.",
        "}": "-.--.-", ";": "-.-.-."
    }

    morse_decode = {v: k for k, v in morse_characters.items()}

    @classmethod
    def msg(cls, lines, encode):
        cls.message = []
        for line in lines:
            cls.message.append("")
            if encode:
                for character in line:
                    if (character.upper() in cls.morse_characters):
                        cls.message[-1] += cls.morse_characters[character.upper()] + " "
            else:
                for character in line.split():
                    if (character.upper() in cls.morse_decode):
                        cls.message[-1] += cls.morse_decode[character.upper()]
            cls.message[-1] += "\n"
        return cls.message

