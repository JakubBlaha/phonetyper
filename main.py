from typing import List


DICT = ["o", "co", "meles", "podivej", "se",
        "na", "sebe", "je", "ti", "dost", "teda", "no"]

CHAR_TO_DIGIT = {
    'a': '2',
    'b': '2',
    'c': '2',
    'd': '3',
    'e': '3',
    'f': '3',
    'g': '4',
    'h': '4',
    'i': '4',
    'j': '5',
    'k': '5',
    'l': '5',
    'm': '6',
    'n': '6',
    'o': '6',
    'p': '7',
    'q': '7',
    'r': '7',
    's': '7',
    't': '8',
    'u': '8',
    'v': '8',
    'w': '9',
    'x': '9',
    'y': '9',
    'z': '9'
}

SEQ = "26 63537"


class Parser:
    buffer: List[str]
    dictionary: list[str]

    def __init__(self) -> None:
        self.buffer = []
        self.dictionary = {}

    def load_dict(self, fname: str):
        with open(fname) as f:
            lines = f.readlines()

        self.dictionary = [l.strip() for l in lines]

    def extend_dict(self, words: List[str]):
        self.dictionary.extend(words)

    def register_digit(self, digit: str) -> None:
        self.buffer.append(digit)

    def resolve_buffer(self) -> str:
        words = []
        buffer_len = len(self.buffer)

        for word in self.dictionary:
            if len(word) == buffer_len:
                words.append(word)

        words = Parser.resolve_recursively(
            self.buffer, 0, buffer_len - 1, words)

        self.buffer.clear()

        return words

    @staticmethod
    def resolve_recursively(buffer: List[str], index: int, last_index: int, words: List[str]):
        if index > last_index:
            return words

        for word in words.copy():
            try:
                if CHAR_TO_DIGIT[word[index]] != buffer[index]:
                    words.remove(word)
            except KeyError:
                words.remove(word)

        return Parser.resolve_recursively(buffer, index + 1, last_index, words)

    def _flatten_res(self, words: List[List[str]]):
        flat = [i[0] for i in words if i]

        return ' '.join(flat)

    def resolve_string(self, s: str) -> str:
        print('Resolving: ', s)

        words = []

        for ch in s:
            if ch in ' 0':
                words.append(self.resolve_buffer())
                continue

            self.register_digit(ch)

        words.append(self.resolve_buffer())

        print(words)

        return self._flatten_res(words)


def main():
    user_input = input("Enter digits: ")

    parser = Parser()
    resolved = parser.resolve_string(user_input)

    print(resolved)


if __name__ == "__main__":
    main()
