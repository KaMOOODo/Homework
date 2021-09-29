"""Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed,
then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up,
whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key."""


class Cipher:
    __alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    __cipher = []

    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.__set_cipher(self.keyword)

    def __set_cipher(self, keyword):
        self.__cipher.extend(x for x in keyword if x not in self.__cipher)
        self.__cipher.extend(x for x in self.__alphabet if x not in self.__cipher)

    def encode(self, string_to_encode):
        encode_str = []
        for char in string_to_encode:
            try:
                index = self.__alphabet.index(char.upper())
                if char.isupper():
                    encode_str.append(self.__cipher[index].upper())
                else:
                    encode_str.append(self.__cipher[index].lower())
            except ValueError:
                encode_str.append(char)

        return print("".join(encode_str))

    def decode(self, string_to_decode):
        decode_str = []
        for char in string_to_decode:
            try:
                index = self.__cipher.index(char.upper())
                if char.isupper():
                    decode_str.append(self.__alphabet[index].upper())
                else:
                    decode_str.append(self.__alphabet[index].lower())
            except ValueError:
                decode_str.append(char)

        return print("".join(decode_str))

cipher = Cipher("crypto")
cipher.encode("Hello world")
# "Btggj vjmgp"
#
cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
