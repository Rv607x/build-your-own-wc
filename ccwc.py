"""
CCWC (Command-line Character Word Counter)

A Python implementation of the Unix 'wc' utility that provides statistics about text files.
This module allows counting bytes, lines, words, and characters in text files through
a command-line interface.

Features:
    - Count number of bytes (-c)
    - Count number of lines (-l) 
    - Count number of words (-w)
    - Count number of characters (-m)
    - Default mode showing bytes, lines and words together

Usage:
    python ccwc.py [-h] [-c FILE] [-l FILE] [-w FILE] [-m FILE] [file]

Example:
    python ccwc.py -l myfile.txt    # Count lines in myfile.txt
    python ccwc.py myfile.txt       # Show default statistics
"""
import argparse


class Ccwc:
    """A command line word count tool that analyzes text files.
    This class provides functionality similar to Unix's wc command,
    allowing counting of bytes, lines, words, and characters in text files.

    Attributes:
        path (str): The file path to analyze
    """

    def __init__(self, path):
        """Initialize the Ccwc instance with a file path.

        Args:
            path (str): Path to the text file to analyze
        """
        self.path = path

    def number_of_lines(self):
        """Count the total number of lines in the file.

        Returns:
            int: The number of lines in the file
        """
        with open(self.path, "r", encoding="utf-8") as file:
            lines = len(file.readlines())
        return lines

    def number_of_bytes(self):
        """Count the total number of bytes in the file.

        Returns:
            int: The number of bytes in the file
        """
        with open(self.path, "rb") as file:
            file_content = file.read()
            return len(file_content)

    def number_of_words(self):
        """Count the total number of words in the file.

        Words are considered as space-separated sequences of characters.

        Returns:
            int: The number of words in the file
        """
        with open(self.path, "r", encoding="utf-8") as file:
            file_content = file.read()
        return len(file_content.split())

    def number_of_chars(self):
        """Count the total number of characters in the file.

        Handles UTF-8 encoding and accounts for special cases like BOMs
        and newline characters.

        Returns:
            int: The number of characters in the file
        """
        char_count = 0
        with open(self.path, "r", encoding="utf-8") as file:
            for line in file:
                char_count += len(line)
                char_count += 1
        return char_count

    def default_mode(self):
        """Provide a default analysis of the file including bytes, lines, and words.

        Returns:
            str: A space-separated string containing the number of bytes, lines,
                 words, and the file path
        """
        lines = self.number_of_lines()
        words = self.number_of_words()
        num_of_bytes = self.number_of_bytes()
        return f"{num_of_bytes} {lines} {words} {self.path}"

def main():
    """Process command line arguments and execute the requested word count operation.

    This function sets up the argument parser, processes the command line arguments,
    and calls the appropriate Ccwc methods based on the provided flags.

    Command line options:
        -help: Show usage instructions
        -c: Count bytes
        -l: Count lines
        -w: Count words
        -m: Count characters
        No flag: Show default analysis (bytes, lines, words and file name)
    """
    parser = argparse.ArgumentParser(
        description="""ccwc - A clone of unix WC tool used to view count of words, characters,
        lines and bytes of a text file"""
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
