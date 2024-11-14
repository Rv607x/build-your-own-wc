import argparse


class Ccwc:
    """test doc"""

    def __init__(self, path):
        """test doc"""
        self.path = path

    def number_of_lines(self):
        """test doc"""
        with open(self.path, "r", encoding="utf-8") as file:
            lines = len(file.readlines())
        return lines

    def number_of_bytes(self):
        """test doc"""
        with open(self.path, "rb") as file:
            file_content = file.read()
            return len(file_content)

    def number_of_words(self):
        """test doc"""
        with open(self.path, "r", encoding="utf-8") as file:
            file_content = file.read()
        return len(file_content.split())

    def number_of_chars(self):
        """test doc"""
        with open(
            self.path, "rb"
        ) as file:  # Open in binary mode to handle all bytes directly
            file_content = file.read()
        # Decode the content, ignoring any BOM or unusual markers
        text = file_content.decode("utf-8-sig")
        num_of_chars = len(text)
        if file_content.endswith(b"\n") and not text.endswith("\n"):
            num_of_chars += 1
        return num_of_chars

    def default_mode(self):
        lines = self.number_of_lines()
        words = self.number_of_words()
        # chars = self.number_of_chars()
        num_of_bytes = self.number_of_bytes()
        return (
            str(num_of_bytes)
            + (" ")
            + str(lines)
            + (" ")
            + str(words)
            + (" ")
            + self.path
        )


def main():
    parser = argparse.ArgumentParser(
        description="ccwc - A clone of unix WC tool used to view count of words, characters, lines and bytes of a text file"
    )
    parser.add_argument("-help", action="store_true", help="Show list of commands")
    parser.add_argument(
        "file", nargs="?", help="The text file to analyze in default mode"
    )

    parser.add_argument(
        "-c", metavar="FILE", help="Show number of bytes in the specified file"
    )
    parser.add_argument(
        "-l", metavar="FILE", help="Show number of lines in the specified file"
    )
    parser.add_argument(
        "-w", metavar="FILE", help="Show number of words in the specified file"
    )
    parser.add_argument(
        "-m", metavar="FILE", help="Show number of characters in the specified file"
    )
    args = parser.parse_args()

    if args.help:
        print("Usage:")
        print("  ccwc -help Show list of")
        print("  ccwc -c Show number of bytes in the specified file")
        print("  ccwc -l Show number of lines in the specified file")
        print("  ccwc -w Show number of words in the specified file")
        print("  ccwc -m Show number of characters in the specified file")

    elif args.c:
        analyzer = Ccwc(args.c)
        print(analyzer.number_of_bytes())

    elif args.l:
        analyzer = Ccwc(args.l)
        print(analyzer.number_of_lines())

    elif args.w:
        analyzer = Ccwc(args.w)
        print(analyzer.number_of_words())

    elif args.m:
        analyzer = Ccwc(args.m)
        print(analyzer.number_of_chars())

    elif args.file:
        analyzer = Ccwc(args.file)
        print(analyzer.default_mode())

    else:
        print("Invalid command. Kindly use -help to see list of available commands")


if __name__ == "__main__":
    main()
