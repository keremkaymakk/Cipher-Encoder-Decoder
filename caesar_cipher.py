class Caesar:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def msg(cls, lines, encode):
        cls.message = []
        for line in lines:
            cls.message.append("")
            for char in line:
                if char.upper() in cls.alphabet:
                    if encode:
                        cls.message[-1] += cls.alphabet[(cls.alphabet.index(char.upper()) + 3) % 26]
                    else:
                        cls.message[-1] += cls.alphabet[(cls.alphabet.index(char.upper()) - 3) % 26]
                elif char != "\n":
                    cls.message[-1] += char
            cls.message[-1] += "\n"
        return cls.message

